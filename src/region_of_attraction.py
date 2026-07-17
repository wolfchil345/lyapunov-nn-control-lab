from collections.abc import Callable

import numpy as np

from src.simulation import simulate


def evaluate_region_of_attraction(
    controller: Callable[[np.ndarray], float],
    position_range: tuple[float, float] = (-2.5, 2.5),
    velocity_range: tuple[float, float] = (-2.5, 2.5),
    num_points: int = 15,
    convergence_threshold: float = 0.1,
    duration: float = 8.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Evaluate convergence over a grid of initial states."""

    if num_points < 2:
        raise ValueError("num_points must be at least 2.")

    if convergence_threshold <= 0.0:
        raise ValueError("convergence_threshold must be positive.")

    positions = np.linspace(
        position_range[0],
        position_range[1],
        num_points,
    )
    velocities = np.linspace(
        velocity_range[0],
        velocity_range[1],
        num_points,
    )

    convergence_map = np.zeros(
        (num_points, num_points),
        dtype=bool,
    )
    final_norm_map = np.zeros(
        (num_points, num_points),
        dtype=float,
    )

    for velocity_index, velocity in enumerate(velocities):
        for position_index, position in enumerate(positions):
            initial_state = np.array([position, velocity])

            solution = simulate(
                controller,
                initial_state,
                duration=duration,
            )

            final_norm = np.linalg.norm(solution.y[:, -1])
            final_norm_map[velocity_index, position_index] = final_norm

            convergence_map[velocity_index, position_index] = (
                solution.success
                and final_norm < convergence_threshold
            )

    return positions, velocities, convergence_map, final_norm_map
