from collections.abc import Callable

import numpy as np
from scipy.integrate import solve_ivp

from src.system import A, B


def simulate(
    controller: Callable[[np.ndarray], float],
    x0: np.ndarray,
    duration: float = 10.0,
):
    """Simulate closed-loop dynamics."""

    def closed_loop_rhs(_t: float, x: np.ndarray) -> np.ndarray:
        u = controller(x)
        return A @ x + B[:, 0] * u

    t_eval = np.linspace(0.0, duration, 1001)

    return solve_ivp(
        closed_loop_rhs,
        (0.0, duration),
        x0,
        t_eval=t_eval,
        rtol=1e-8,
        atol=1e-10,
    )
