from collections.abc import Callable

import numpy as np
from scipy.integrate import trapezoid

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
    """Calculate quantitative closed-loop performance metrics."""

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

    state_norms = np.linalg.norm(states, axis=1)

    # Settling time:
    # first time after which the state norm remains below the threshold.
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

    # Quadratic LQR-style cost:
    # integral of x^T Q x + u^T R u.
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

    control_energy = trapezoid(
        controls**2,
        time,
    )

    return {
        "final_state_norm": float(state_norms[-1]),
        "settling_time_s": settling_time,
        "quadratic_cost": float(quadratic_cost),
        "control_energy": float(control_energy),
        "max_abs_control": float(
            np.max(np.abs(controls))
        ),
    }
