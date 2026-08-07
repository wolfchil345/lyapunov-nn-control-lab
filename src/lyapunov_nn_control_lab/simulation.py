from collections.abc import Callable

import numpy as np
from scipy.integrate import solve_ivp

from .system import A, B
from ._validation import (
    evaluate_controller,
    validate_controller,
    validate_positive_scalar,
    validate_state,
)


def simulate(
    controller: Callable[[np.ndarray], float],
    x0: np.ndarray,
    duration: float = 10.0,
):
    """Simulate closed-loop dynamics over normalized time."""

    controller = validate_controller(controller)
    initial_state = validate_state(x0, name="initial state")
    duration = validate_positive_scalar(duration, name="duration")

    def closed_loop_rhs(_t: float, x: np.ndarray) -> np.ndarray:
        state = validate_state(x, name="simulation state")
        control = evaluate_controller(controller, state)
        return A @ state + B[:, 0] * control

    t_eval = np.linspace(0.0, duration, 1001)

    return solve_ivp(
        closed_loop_rhs,
        (0.0, duration),
        initial_state,
        t_eval=t_eval,
        rtol=1e-8,
        atol=1e-10,
    )
