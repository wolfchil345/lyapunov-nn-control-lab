from collections.abc import Callable

import numpy as np

from src.system import A, B, P


def lyapunov_value(x: np.ndarray) -> float:
    """V(x) = x^T P x."""
    return float(x.T @ P @ x)


def lyapunov_derivative(
    x: np.ndarray,
    controller: Callable[[np.ndarray], float],
) -> float:
    """Vdot(x) = 2 x^T P f(x)."""
    u = controller(x)
    closed_loop_vector_field = A @ x + B[:, 0] * u
    return float(2.0 * x.T @ P @ closed_loop_vector_field)


def grid_check(controller: Callable[[np.ndarray], float]) -> dict[str, float]:
    """Empirically inspect V-dot on a rectangular state-space grid."""
    positions = np.linspace(-2.0, 2.0, 81)
    velocities = np.linspace(-3.0, 3.0, 81)

    vdots: list[float] = []

    for position in positions:
        for velocity in velocities:
            x = np.array([position, velocity], dtype=float)

            if np.linalg.norm(x) < 1e-9:
                continue

            vdots.append(lyapunov_derivative(x, controller))

    values = np.asarray(vdots)

    return {
        "maximum_vdot": float(values.max()),
        "violation_fraction": float(np.mean(values > 1e-6)),
    }
