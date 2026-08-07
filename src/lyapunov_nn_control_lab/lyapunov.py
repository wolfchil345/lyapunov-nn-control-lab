from collections.abc import Callable

import numpy as np

from .system import A, B, P
from ._validation import evaluate_controller, validate_controller, validate_state


def lyapunov_value(x: np.ndarray) -> float:
    """V(x) = x^T P x."""
    state = validate_state(x)
    return float(state.T @ P @ state)


def lyapunov_derivative(
    x: np.ndarray,
    controller: Callable[[np.ndarray], float],
) -> float:
    """Vdot(x) = 2 x^T P f(x)."""
    controller = validate_controller(controller)
    state = validate_state(x)
    control = evaluate_controller(controller, state)
    closed_loop_vector_field = A @ state + B[:, 0] * control
    return float(2.0 * state.T @ P @ closed_loop_vector_field)


def grid_check(controller: Callable[[np.ndarray], float]) -> dict[str, float]:
    """Empirically inspect V-dot on a rectangular state-space grid."""
    controller = validate_controller(controller)
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
