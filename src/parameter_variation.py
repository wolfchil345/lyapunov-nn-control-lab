from collections.abc import Callable

import numpy as np
from scipy.integrate import solve_ivp

from src.validation import nonnegative_number, positive_number, state_vector


def make_state_space_matrices(
    mass: float,
    damping: float,
    stiffness: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Create state-space matrices for a mass-spring-damper system."""

    mass = positive_number(mass, name="mass")
    damping = nonnegative_number(damping, name="damping")
    stiffness = positive_number(stiffness, name="stiffness")

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

    initial_state = state_vector(initial_state, name="initial_state")
    duration = positive_number(duration, name="duration")

    a_matrix, b_matrix = make_state_space_matrices(
        mass=mass,
        damping=damping,
        stiffness=stiffness,
    )

    def closed_loop_rhs(_time: float, state: np.ndarray) -> np.ndarray:
        control = controller(state)
        if not np.isfinite(control):
            raise ValueError("controller returned a non-finite control input.")
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
