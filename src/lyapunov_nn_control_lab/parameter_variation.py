from collections.abc import Callable

import numpy as np
from scipy.integrate import solve_ivp


def make_state_space_matrices(
    mass: float,
    damping: float,
    stiffness: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Create state-space matrices for a mass-spring-damper system."""

    if mass <= 0.0:
        raise ValueError("Mass must be positive.")

    if damping < 0.0:
        raise ValueError("Damping must be nonnegative.")

    if stiffness <= 0.0:
        raise ValueError("Stiffness must be positive.")

    a_matrix = np.array(
        [
            [0.0, 1.0],
            [-stiffness / mass, -damping / mass],
        ],
        dtype=float,
    )

    b_matrix = np.array(
        [[0.0], [1.0 / mass]],
        dtype=float,
    )

    return a_matrix, b_matrix


def simulate_parameter_variation(
    controller: Callable[[np.ndarray], float],
    initial_state: np.ndarray,
    mass: float,
    damping: float,
    stiffness: float,
    duration: float = 10.0,
):
    """Simulate closed-loop dynamics under changed plant parameters."""

    a_matrix, b_matrix = make_state_space_matrices(
        mass=mass,
        damping=damping,
        stiffness=stiffness,
    )

    def closed_loop_rhs(_time: float, state: np.ndarray) -> np.ndarray:
        control = controller(state)
        return a_matrix @ state + b_matrix[:, 0] * control

    time_points = np.linspace(0.0, duration, 1001)

    return solve_ivp(
        closed_loop_rhs,
        (0.0, duration),
        initial_state,
        t_eval=time_points,
        rtol=1e-8,
        atol=1e-10,
    )
