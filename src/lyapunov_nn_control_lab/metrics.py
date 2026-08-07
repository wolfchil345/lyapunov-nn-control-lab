from collections.abc import Callable

import numpy as np
from scipy.integrate import trapezoid

from .state_coordinates import state_norm
from .system import Q, R
from ._validation import (
    evaluate_controller,
    validate_controller,
    validate_positive_scalar,
)


def calculate_metrics(
    solution,
    controller: Callable[[np.ndarray], float],
    settling_threshold: float = 0.02,
) -> dict[str, float]:
    """Calculate metrics in the normalized coordinate and time convention.

    Settling time is the first sample after the last sample outside the closed
    tolerance set ``||x||_2 <= settling_threshold``. Consequently, every later
    sampled state remains inside the set. ``settling_time_s`` and
    ``control_energy`` are retained as compatibility aliases only.
    """

    if not solution.success:
        raise ValueError("Cannot calculate metrics for a failed simulation.")

    controller = validate_controller(controller)
    settling_threshold = validate_positive_scalar(
        settling_threshold,
        name="settling_threshold",
    )

    time = np.asarray(solution.t, dtype=float)
    raw_states = np.asarray(solution.y, dtype=float)
    if time.ndim != 1 or time.size == 0:
        raise ValueError("solution.t must be a nonempty one-dimensional array.")
    if raw_states.ndim != 2 or raw_states.shape[0] != 2:
        raise ValueError("solution.y must have shape (2, number_of_samples).")
    if raw_states.shape[1] != time.size:
        raise ValueError("solution.t and solution.y must contain the same samples.")
    if not np.all(np.isfinite(time)) or not np.all(np.isfinite(raw_states)):
        raise ValueError("solution data must contain only finite values.")
    states = raw_states.T
    controls = np.array(
        [evaluate_controller(controller, state) for state in states],
        dtype=float,
    )

    return calculate_metrics_from_control_samples(
        solution,
        controls,
        settling_threshold=settling_threshold,
    )


def calculate_metrics_from_control_samples(
    solution,
    controls: np.ndarray,
    settling_threshold: float = 0.02,
) -> dict[str, float]:
    """Calculate metrics using control samples recorded during simulation.

    This is used by stochastic measurement-noise simulations so the reported
    control quantities reflect the noisy measurements actually supplied to the
    controller rather than a later noise-free replay.
    """

    if not solution.success:
        raise ValueError("Cannot calculate metrics for a failed simulation.")
    settling_threshold = validate_positive_scalar(
        settling_threshold,
        name="settling_threshold",
    )

    time = np.asarray(solution.t, dtype=float)
    raw_states = np.asarray(solution.y, dtype=float)
    controls = np.asarray(controls, dtype=float)
    if time.ndim != 1 or time.size == 0:
        raise ValueError("solution.t must be a nonempty one-dimensional array.")
    if raw_states.ndim != 2 or raw_states.shape[0] != 2:
        raise ValueError("solution.y must have shape (2, number_of_samples).")
    if raw_states.shape[1] != time.size:
        raise ValueError("solution.t and solution.y must contain the same samples.")
    if controls.ndim != 1 or controls.size != time.size:
        raise ValueError(
            "controls must be one-dimensional with one value per solution sample."
        )
    if (
        not np.all(np.isfinite(time))
        or not np.all(np.isfinite(raw_states))
        or not np.all(np.isfinite(controls))
    ):
        raise ValueError("solution data and controls must contain only finite values.")
    states = raw_states.T

    state_norms = np.array([state_norm(state) for state in states])

    # Settling time: first normalized time after which the normalized-state
    # norm remains inside the closed tolerance set.
    outside_threshold = np.flatnonzero(
        state_norms > settling_threshold
    )

    if outside_threshold.size == 0:
        settling_time = 0.0
    elif outside_threshold[-1] == len(time) - 1:
        settling_time = float("nan")
    else:
        settling_time = float(
            time[outside_threshold[-1] + 1]
        )

    # Dimensionless LQR-style objective: integral of x^T Q x + u^T R u
    # over normalized time. Q and R are objective weights, not physical units.
    state_penalty = np.einsum(
        "ni,ij,nj->n",
        states,
        Q,
        states,
    )

    control_penalty = float(R.item()) * controls**2

    quadratic_cost = trapezoid(
        state_penalty + control_penalty,
        time,
    )

    integrated_squared_control_effort = trapezoid(
        controls**2,
        time,
    )

    return {
        "final_state_norm": float(state_norms[-1]),
        "settling_time": settling_time,
        # Compatibility alias: historical files used an SI-looking suffix.
        "settling_time_s": settling_time,
        "quadratic_cost": float(quadratic_cost),
        "integrated_squared_control_effort": float(
            integrated_squared_control_effort
        ),
        # Compatibility alias: this integral is not physical energy.
        "control_energy": float(integrated_squared_control_effort),
        "max_abs_control": float(
            np.max(np.abs(controls))
        ),
    }
