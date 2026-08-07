from collections.abc import Callable
from dataclasses import dataclass

import numpy as np

from .system import A, B, P
from ._validation import (
    evaluate_controller,
    validate_controller,
    validate_finite_scalar,
    validate_nonnegative_scalar,
    validate_state,
)


DEFAULT_DECAY_MARGIN = 0.05
DEFAULT_NUMERICAL_TOLERANCE = 1e-9


@dataclass(frozen=True)
class LyapunovSampleEvaluation:
    """Evaluation of the basic and decay-margin conditions at one state."""

    vdot: float
    decay_residual: float
    derivative_violation: bool
    decay_margin_violation: bool


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


def lyapunov_decay_residual(
    x: np.ndarray,
    vdot: float,
    decay_margin: float = DEFAULT_DECAY_MARGIN,
) -> float:
    """Return V-dot + decay_margin * ||x||^2 for one state."""

    state = validate_state(x)
    vdot = validate_finite_scalar(vdot, name="vdot")
    decay_margin = validate_nonnegative_scalar(
        decay_margin,
        name="decay_margin",
    )
    return float(vdot + decay_margin * np.dot(state, state))


def evaluate_lyapunov_sample(
    x: np.ndarray,
    vdot: float,
    *,
    decay_margin: float = DEFAULT_DECAY_MARGIN,
    numerical_tolerance: float = DEFAULT_NUMERICAL_TOLERANCE,
) -> LyapunovSampleEvaluation:
    """Classify one sample under both Lyapunov decrease conditions.

    ``numerical_tolerance`` only handles floating-point noise. It is separate
    from ``decay_margin``, which defines the requested scientific decay rate.
    """

    state = validate_state(x)
    vdot = validate_finite_scalar(vdot, name="vdot")
    decay_margin = validate_nonnegative_scalar(
        decay_margin,
        name="decay_margin",
    )
    numerical_tolerance = validate_nonnegative_scalar(
        numerical_tolerance,
        name="numerical_tolerance",
    )
    residual = lyapunov_decay_residual(state, vdot, decay_margin)
    return LyapunovSampleEvaluation(
        vdot=vdot,
        decay_residual=residual,
        derivative_violation=vdot > numerical_tolerance,
        decay_margin_violation=residual > numerical_tolerance,
    )


def grid_check(
    controller: Callable[[np.ndarray], float],
    *,
    decay_margin: float = DEFAULT_DECAY_MARGIN,
    numerical_tolerance: float = DEFAULT_NUMERICAL_TOLERANCE,
) -> dict[str, float | int]:
    """Evaluate two Lyapunov conditions on a finite rectangular grid.

    The exact equilibrium is excluded because V(0) = V-dot(0) = 0. Every
    other sampled state is evaluated; no neighborhood is hidden. Results are
    empirical sampled evidence, not a continuous-state stability proof.
    """

    controller = validate_controller(controller)
    decay_margin = validate_nonnegative_scalar(
        decay_margin,
        name="decay_margin",
    )
    numerical_tolerance = validate_nonnegative_scalar(
        numerical_tolerance,
        name="numerical_tolerance",
    )
    positions = np.linspace(-2.0, 2.0, 81)
    velocities = np.linspace(-3.0, 3.0, 81)

    vdots: list[float] = []
    residuals: list[float] = []
    derivative_violation_count = 0
    decay_margin_violation_count = 0

    for position in positions:
        for velocity in velocities:
            x = np.array([position, velocity], dtype=float)

            if position == 0.0 and velocity == 0.0:
                continue

            sample = evaluate_lyapunov_sample(
                x,
                lyapunov_derivative(x, controller),
                decay_margin=decay_margin,
                numerical_tolerance=numerical_tolerance,
            )
            vdots.append(sample.vdot)
            residuals.append(sample.decay_residual)
            derivative_violation_count += int(sample.derivative_violation)
            decay_margin_violation_count += int(sample.decay_margin_violation)

    vdot_values = np.asarray(vdots)
    residual_values = np.asarray(residuals)
    sample_count = len(vdots)

    return {
        "sample_count": sample_count,
        "decay_margin": decay_margin,
        "numerical_tolerance": numerical_tolerance,
        "max_vdot": float(vdot_values.max()),
        "max_decay_residual": float(residual_values.max()),
        "derivative_violation_count": derivative_violation_count,
        "derivative_violation_fraction": (
            derivative_violation_count / sample_count
        ),
        "decay_margin_violation_count": decay_margin_violation_count,
        "decay_margin_violation_fraction": (
            decay_margin_violation_count / sample_count
        ),
    }
