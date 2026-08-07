"""Deprecated compatibility interface for finite-horizon convergence."""

from __future__ import annotations

from collections.abc import Callable
import warnings

import numpy as np

from .finite_horizon_convergence import (
    FiniteHorizonConvergenceResult,
    evaluate_finite_horizon_convergence,
)


def evaluate_region_of_attraction(
    controller: Callable[[np.ndarray], float],
    position_range: tuple[float, float] = (-2.5, 2.5),
    velocity_range: tuple[float, float] = (-2.5, 2.5),
    num_points: int = 15,
    convergence_threshold: float = 0.1,
    duration: float = 8.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return the legacy tuple after a deprecated finite-horizon evaluation."""

    warnings.warn(
        "evaluate_region_of_attraction() is deprecated because its name was "
        "mathematically misleading for a finite-horizon final-state tolerance "
        "test; use "
        "evaluate_finite_horizon_convergence() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    result: FiniteHorizonConvergenceResult = (
        evaluate_finite_horizon_convergence(
            controller,
            position_bounds=position_range,
            velocity_bounds=velocity_range,
            grid_resolution=num_points,
            convergence_tolerance=convergence_threshold,
            horizon=duration,
        )
    )
    return (
        result.positions,
        result.velocities,
        result.convergence_map,
        result.final_norm_map,
    )
