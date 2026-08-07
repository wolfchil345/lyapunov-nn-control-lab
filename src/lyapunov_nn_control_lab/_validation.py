from __future__ import annotations

from collections.abc import Callable, Sequence
from numbers import Integral
from typing import Any

import numpy as np


MAX_TIME_GRID_POINTS = 1_000_001


def validate_state(value: Any, *, name: str = "state") -> np.ndarray:
    """Return a finite two-element real state vector."""

    if isinstance(value, (str, bytes)):
        raise TypeError(f"{name} must be a numeric one-dimensional vector.")

    try:
        state = np.asarray(value)
    except (TypeError, ValueError) as exc:
        raise TypeError(
            f"{name} must be a numeric one-dimensional vector."
        ) from exc

    if state.dtype.kind not in "fiu":
        raise TypeError(f"{name} must contain real numeric values.")
    if state.ndim != 1 or state.shape != (2,):
        raise ValueError(
            f"{name} must have shape (2,) for [position, velocity]; "
            f"received shape {state.shape}."
        )

    state = state.astype(float, copy=False)
    if not np.all(np.isfinite(state)):
        raise ValueError(f"{name} must contain only finite values.")
    return state


def validate_finite_scalar(value: Any, *, name: str) -> float:
    """Return a finite real scalar."""

    if isinstance(value, (str, bytes)):
        raise TypeError(f"{name} must be a real scalar.")

    try:
        scalar = np.asarray(value)
    except (TypeError, ValueError) as exc:
        raise TypeError(f"{name} must be a real scalar.") from exc

    if scalar.ndim != 0:
        raise ValueError(
            f"{name} must be a scalar; received shape {scalar.shape}."
        )
    if scalar.dtype.kind not in "fiu":
        raise TypeError(f"{name} must be a real scalar.")

    result = float(scalar)
    if not np.isfinite(result):
        raise ValueError(f"{name} must be finite.")
    return result


def validate_positive_scalar(value: Any, *, name: str) -> float:
    """Return a finite scalar greater than zero."""

    result = validate_finite_scalar(value, name=name)
    if result <= 0.0:
        raise ValueError(f"{name} must be positive.")
    return result


def validate_nonnegative_scalar(value: Any, *, name: str) -> float:
    """Return a finite scalar greater than or equal to zero."""

    result = validate_finite_scalar(value, name=name)
    if result < 0.0:
        raise ValueError(f"{name} must be nonnegative.")
    return result


def validate_controller(controller: Any) -> Callable[[np.ndarray], Any]:
    """Require a callable controller."""

    if not callable(controller):
        raise TypeError("controller must be callable.")
    return controller


def evaluate_controller(
    controller: Callable[[np.ndarray], Any],
    state: np.ndarray,
) -> float:
    """Evaluate a controller and require a finite scalar result."""

    output = controller(state)
    return validate_finite_scalar(output, name="controller output")


def validate_seed(seed: Any) -> int:
    """Return a nonnegative integer random seed."""

    if isinstance(seed, bool) or not isinstance(seed, Integral):
        raise TypeError("seed must be a nonnegative integer.")
    result = int(seed)
    if result < 0:
        raise ValueError("seed must be a nonnegative integer.")
    return result


def build_time_grid(
    duration: float,
    dt: float,
    *,
    max_points: int = MAX_TIME_GRID_POINTS,
) -> np.ndarray:
    """Build a bounded grid that starts at zero and ends at duration."""

    duration = validate_positive_scalar(duration, name="duration")
    dt = validate_positive_scalar(dt, name="dt")

    step_ratio = duration / dt
    if not np.isfinite(step_ratio) or step_ratio > max_points - 1:
        estimated_points = f"more than {max_points}"
        raise ValueError(
            "Requested time grid is too large: "
            f"{estimated_points} points exceeds the limit of {max_points}."
        )
    estimated_points = int(np.ceil(step_ratio)) + 1

    full_steps = int(np.floor(duration / dt))
    time = np.arange(full_steps + 1, dtype=float) * dt
    tolerance = max(
        8.0 * np.finfo(float).eps * max(1.0, abs(duration)),
        8.0 * np.spacing(duration),
    )

    if np.isclose(time[-1], duration, rtol=0.0, atol=tolerance):
        time[-1] = duration
    else:
        time = np.append(time, duration)

    if np.any(time > duration):
        raise RuntimeError("Time-grid construction exceeded the duration.")
    return time


def require_nonempty(values: Sequence[Any], *, name: str) -> None:
    """Require a nonempty sized collection."""

    if len(values) == 0:
        raise ValueError(f"{name} must not be empty.")


def require_matching_lengths(
    first: Sequence[Any],
    second: Sequence[Any],
    *,
    first_name: str,
    second_name: str,
) -> None:
    """Require two sized collections to have the same nonzero length."""

    require_nonempty(first, name=first_name)
    require_nonempty(second, name=second_name)
    if len(first) != len(second):
        raise ValueError(
            f"{first_name} and {second_name} must have the same length; "
            f"received {len(first)} and {len(second)}."
        )
