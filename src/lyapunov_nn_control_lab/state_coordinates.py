"""Normalized state-coordinate convention and shared magnitude helpers."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import torch

from ._validation import validate_state


@dataclass(frozen=True)
class StateCoordinateConvention:
    """Metadata for the dimensionless coordinates used by the model."""

    name: str
    time_symbol: str
    position_symbol: str
    velocity_symbol: str
    control_symbol: str
    dimensionless: bool


NORMALIZED_STATE_CONVENTION = StateCoordinateConvention(
    name="normalized dimensionless second-order coordinates",
    time_symbol="tau",
    position_symbol="q",
    velocity_symbol="v = dq/dtau",
    control_symbol="u",
    dimensionless=True,
)

NORMALIZED_TIME_LABEL = "Normalized time"
NORMALIZED_POSITION_LABEL = "Normalized position q"
NORMALIZED_VELOCITY_LABEL = "Normalized velocity v"
NORMALIZED_CONTROL_LABEL = "Normalized control input u"
NORMALIZED_STATE_NORM_LABEL = "Normalized state norm ||x||_2"


def squared_state_norm(x: object) -> float:
    """Return ``q**2 + v**2`` for one validated normalized state."""

    state = validate_state(x)
    return float(np.dot(state, state))


def state_norm(x: object) -> float:
    """Return the Euclidean norm of one normalized state ``[q, v]``."""

    return float(np.sqrt(squared_state_norm(x)))


def _validate_torch_states(states: object) -> torch.Tensor:
    """Return finite floating Torch states whose last dimension is two."""

    if not isinstance(states, torch.Tensor):
        raise TypeError("states must be a torch.Tensor.")
    if not states.is_floating_point():
        raise TypeError("states must use a floating-point dtype.")
    if states.ndim == 0 or states.shape[-1] != 2:
        raise ValueError(
            "states must have final dimension 2 for normalized [q, v] states."
        )
    if not bool(torch.isfinite(states).all().item()):
        raise ValueError("states must contain only finite values.")
    return states


def torch_squared_state_norm(states: torch.Tensor) -> torch.Tensor:
    """Return differentiable ``q**2 + v**2`` values for Torch states."""

    states = _validate_torch_states(states)
    return torch.sum(torch.square(states), dim=-1)


def torch_state_norm(states: torch.Tensor) -> torch.Tensor:
    """Return differentiable Euclidean norms for normalized Torch states."""

    return torch.sqrt(torch_squared_state_norm(states))
