"""Sample final-state convergence over an explicit finite horizon."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from numbers import Integral

import numpy as np

from ._validation import validate_controller, validate_positive_scalar
from .simulation import simulate
from .state_coordinates import state_norm


MAX_GRID_INITIAL_STATES = 100_000


@dataclass(frozen=True)
class FiniteHorizonConvergenceResult:
    """Result of a sampled final-state tolerance test at one finite horizon."""

    positions: np.ndarray
    velocities: np.ndarray
    convergence_map: np.ndarray
    final_norm_map: np.ndarray
    horizon: float
    convergence_tolerance: float
    position_bounds: tuple[float, float]
    velocity_bounds: tuple[float, float]
    grid_resolution: int
    tested_count: int
    converged_count: int
    convergence_fraction: float
    controller_label: str | None = None

    @property
    def criterion(self) -> str:
        """Return the exact strict final-state criterion used by the evaluator."""

        return "||x(horizon)||_2 < convergence_tolerance"


def _validate_bounds(
    value: tuple[float, float],
    *,
    name: str,
) -> tuple[float, float]:
    """Return finite, strictly increasing lower and upper bounds."""

    if isinstance(value, (str, bytes)):
        raise TypeError(f"{name} must contain two real numeric values.")
    try:
        values = np.asarray(value)
    except (TypeError, ValueError) as exc:
        raise TypeError(
            f"{name} must contain two real numeric values."
        ) from exc
    if values.dtype.kind not in "fiu":
        raise TypeError(f"{name} must contain two real numeric values.")
    if values.shape != (2,):
        raise ValueError(f"{name} must contain exactly two values.")
    values = values.astype(float, copy=False)
    if not np.all(np.isfinite(values)):
        raise ValueError(f"{name} must contain only finite values.")
    if values[0] >= values[1]:
        raise ValueError(f"{name} must be strictly increasing.")
    return float(values[0]), float(values[1])


def _validate_grid_resolution(value: int) -> int:
    """Return a square-grid resolution with a bounded state count."""

    if isinstance(value, bool) or not isinstance(value, Integral):
        raise TypeError("grid_resolution must be an integer of at least 2.")
    result = int(value)
    if result < 2:
        raise ValueError("grid_resolution must be at least 2.")
    if result * result > MAX_GRID_INITIAL_STATES:
        raise ValueError(
            "grid_resolution creates too many initial states: "
            f"{result * result} exceeds the limit of "
            f"{MAX_GRID_INITIAL_STATES}."
        )
    return result


def _validate_controller_label(value: str | None) -> str | None:
    """Return an optional nonempty controller label."""

    if value is None:
        return None
    if not isinstance(value, str):
        raise TypeError("controller_label must be a string or None.")
    result = value.strip()
    if not result:
        raise ValueError("controller_label must not be empty.")
    return result


def _final_state_from_solution(solution: object, *, horizon: float) -> np.ndarray:
    """Return a finite final state from a successful horizon-complete simulation."""

    if not getattr(solution, "success", False):
        message = getattr(solution, "message", "unknown solver failure")
        raise RuntimeError(f"Finite-horizon simulation failed: {message}")
    if not hasattr(solution, "t") or not hasattr(solution, "y"):
        raise TypeError("simulation result must provide t and y arrays.")

    time = np.asarray(solution.t, dtype=float)
    states = np.asarray(solution.y, dtype=float)
    if time.ndim != 1 or time.size == 0 or not np.all(np.isfinite(time)):
        raise ValueError("simulation time samples must be finite and nonempty.")
    if states.ndim != 2 or states.shape != (2, time.size):
        raise ValueError(
            "simulation states must have shape (2, number of time samples)."
        )
    if not np.all(np.isfinite(states)):
        raise ValueError("simulation states must contain only finite values.")
    if not np.isclose(time[-1], horizon, rtol=1e-9, atol=1e-12):
        raise RuntimeError(
            "simulation did not reach the requested finite horizon: "
            f"expected {horizon}, received {time[-1]}."
        )
    return states[:, -1]


def evaluate_finite_horizon_convergence(
    controller: Callable[[np.ndarray], float],
    position_bounds: tuple[float, float] = (-2.5, 2.5),
    velocity_bounds: tuple[float, float] = (-2.5, 2.5),
    grid_resolution: int = 15,
    convergence_tolerance: float = 0.1,
    horizon: float = 8.0,
    *,
    controller_label: str | None = None,
) -> FiniteHorizonConvergenceResult:
    """Classify states using a strict normalized Euclidean final-state norm.

    This finite-time simulation test is not a region-of-attraction
    computation and does not establish asymptotic convergence.
    """

    controller = validate_controller(controller)
    position_bounds = _validate_bounds(
        position_bounds,
        name="position_bounds",
    )
    velocity_bounds = _validate_bounds(
        velocity_bounds,
        name="velocity_bounds",
    )
    grid_resolution = _validate_grid_resolution(grid_resolution)
    convergence_tolerance = validate_positive_scalar(
        convergence_tolerance,
        name="convergence_tolerance",
    )
    horizon = validate_positive_scalar(horizon, name="horizon")
    controller_label = _validate_controller_label(controller_label)

    positions = np.linspace(*position_bounds, grid_resolution)
    velocities = np.linspace(*velocity_bounds, grid_resolution)
    convergence_map = np.zeros(
        (grid_resolution, grid_resolution),
        dtype=bool,
    )
    final_norm_map = np.zeros(
        (grid_resolution, grid_resolution),
        dtype=float,
    )

    for velocity_index, velocity in enumerate(velocities):
        for position_index, position in enumerate(positions):
            initial_state = np.array([position, velocity], dtype=float)
            solution = simulate(controller, initial_state, duration=horizon)
            final_state = _final_state_from_solution(solution, horizon=horizon)
            final_norm = state_norm(final_state)
            final_norm_map[velocity_index, position_index] = final_norm
            convergence_map[velocity_index, position_index] = (
                final_norm < convergence_tolerance
            )

    tested_count = int(convergence_map.size)
    converged_count = int(np.count_nonzero(convergence_map))

    return FiniteHorizonConvergenceResult(
        positions=positions,
        velocities=velocities,
        convergence_map=convergence_map,
        final_norm_map=final_norm_map,
        horizon=horizon,
        convergence_tolerance=convergence_tolerance,
        position_bounds=position_bounds,
        velocity_bounds=velocity_bounds,
        grid_resolution=grid_resolution,
        tested_count=tested_count,
        converged_count=converged_count,
        convergence_fraction=converged_count / tested_count,
        controller_label=controller_label,
    )
