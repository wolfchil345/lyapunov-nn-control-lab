from collections.abc import Callable

import numpy as np
from scipy.integrate import trapezoid

from src.system import Q, R
from src.validation import positive_number


def calculate_metrics(
    solution,
    controller: Callable[[np.ndarray], float],
    settling_threshold: float = 0.02,
) -> dict[str, float]:
    """Calculate quantitative closed-loop performance metrics."""

    if not solution.success:
        raise ValueError("Cannot calculate metrics for a failed simulation.")

    settling_threshold = positive_number(
        settling_threshold,
        name="settling_threshold",
    )

    time = np.asarray(solution.t, dtype=float)
    states = np.asarray(solution.y, dtype=float).T
    if time.ndim != 1 or time.size < 2 or not np.all(np.isfinite(time)):
        raise ValueError("solution.t must be a finite one-dimensional time vector.")
    if states.shape != (time.size, 2) or not np.all(np.isfinite(states)):
        raise ValueError("solution.y must contain finite states with shape (2, n_times).")
    if np.any(np.diff(time) <= 0.0):
        raise ValueError("solution.t must be strictly increasing.")

    controls = np.array(
        [controller(state) for state in states],
        dtype=float,
    )
    if not np.all(np.isfinite(controls)):
        raise ValueError("controller returned a non-finite control input.")

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
