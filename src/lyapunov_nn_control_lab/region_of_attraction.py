from collections.abc import Callable
from numbers import Integral

import numpy as np

from .simulation import simulate
from ._validation import (
    validate_controller,
    validate_positive_scalar,
)


def _validate_range(
    value: tuple[float, float],
    *,
    name: str,
) -> tuple[float, float]:
    """Validate a finite increasing two-value range."""

    values = np.asarray(value)
    if values.dtype.kind not in "fiu":
        raise TypeError(f"{name} must contain real numeric values.")
    if values.shape != (2,):
        raise ValueError(f"{name} must contain exactly two values.")
    values = values.astype(float, copy=False)
    if not np.all(np.isfinite(values)):
        raise ValueError(f"{name} must contain only finite values.")
    if values[0] >= values[1]:
        raise ValueError(f"{name} must be strictly increasing.")
    return float(values[0]), float(values[1])


def evaluate_region_of_attraction(
    controller: Callable[[np.ndarray], float],
    position_range: tuple[float, float] = (-2.5, 2.5),
    velocity_range: tuple[float, float] = (-2.5, 2.5),
    num_points: int = 15,
    convergence_threshold: float = 0.1,
    duration: float = 8.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Evaluate convergence over a grid of initial states."""

    controller = validate_controller(controller)
    position_range = _validate_range(position_range, name="position_range")
    velocity_range = _validate_range(velocity_range, name="velocity_range")
    if isinstance(num_points, bool) or not isinstance(num_points, Integral):
        raise TypeError("num_points must be an integer of at least 2.")
    if num_points < 2:
        raise ValueError("num_points must be at least 2.")
    convergence_threshold = validate_positive_scalar(
        convergence_threshold,
        name="convergence_threshold",
    )
    duration = validate_positive_scalar(duration, name="duration")

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
