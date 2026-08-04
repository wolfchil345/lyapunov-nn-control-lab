from collections.abc import Callable

import numpy as np
from scipy.integrate import solve_ivp

from src.system import A, B
from src.validation import positive_number, state_vector


def simulate(
    controller: Callable[[np.ndarray], float],
    x0: np.ndarray,
    duration: float = 10.0,
):
    """Simulate closed-loop dynamics."""

    initial_state = state_vector(x0, name="x0")
    duration = positive_number(duration, name="duration")

    def closed_loop_rhs(_t: float, x: np.ndarray) -> np.ndarray:
        u = controller(x)
        if not np.isfinite(u):
            raise ValueError("controller returned a non-finite control input.")
        return A @ x + B[:, 0] * u

    t_eval = np.linspace(0.0, duration, 1001)

    return solve_ivp(
        closed_loop_rhs,
        (0.0, duration),
        initial_state,
        t_eval=t_eval,
        rtol=1e-8,
        atol=1e-10,
    )
