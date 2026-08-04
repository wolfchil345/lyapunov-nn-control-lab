"""Shared validation helpers for numerical experiments."""

from __future__ import annotations

import math

import numpy as np

STATE_DIMENSION = 2


def state_vector(value: np.ndarray, *, name: str = "state") -> np.ndarray:
    """Return a finite two-element state vector."""

    array = np.asarray(value, dtype=float)
    if array.shape != (STATE_DIMENSION,):
        raise ValueError(f"{name} must have shape ({STATE_DIMENSION},).")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values.")
    return array


def positive_number(value: float, *, name: str) -> float:
    """Return a finite strictly positive float."""

    number = float(value)
    if not math.isfinite(number) or number <= 0.0:
        raise ValueError(f"{name} must be a finite positive number.")
    return number


def nonnegative_number(value: float, *, name: str) -> float:
    """Return a finite nonnegative float."""

    number = float(value)
    if not math.isfinite(number) or number < 0.0:
        raise ValueError(f"{name} must be a finite nonnegative number.")
    return number


def ordered_range(value: tuple[float, float], *, name: str) -> tuple[float, float]:
    """Return a finite, strictly increasing numeric range."""

    if len(value) != 2:
        raise ValueError(f"{name} must contain exactly two values.")
    lower, upper = map(float, value)
    if not math.isfinite(lower) or not math.isfinite(upper) or lower >= upper:
        raise ValueError(f"{name} must be finite and strictly increasing.")
    return lower, upper
