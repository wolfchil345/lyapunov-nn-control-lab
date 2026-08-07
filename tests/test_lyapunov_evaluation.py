from __future__ import annotations

import numpy as np
import pytest

from lyapunov_nn_control_lab.lyapunov import (
    DEFAULT_DECAY_MARGIN,
    DEFAULT_NUMERICAL_TOLERANCE,
    evaluate_lyapunov_sample,
    grid_check,
    lyapunov_decay_residual,
    lyapunov_derivative,
    lyapunov_value,
)
from lyapunov_nn_control_lab.system import A, B, K, P, lqr_controller


def test_lyapunov_value_matches_quadratic_formula():
    state = np.array([0.75, -1.25])

    assert lyapunov_value(state) == pytest.approx(state.T @ P @ state)


def test_lyapunov_derivative_matches_closed_loop_formula():
    state = np.array([0.5, -0.25])
    control = 0.75
    controller = lambda _state: control
    vector_field = A @ state + B[:, 0] * control

    assert lyapunov_derivative(state, controller) == pytest.approx(
        2.0 * state.T @ P @ vector_field
    )


def test_decay_residual_matches_training_condition():
    state = np.array([3.0, 4.0])

    assert lyapunov_decay_residual(state, -2.0, 0.05) == pytest.approx(-0.75)


def test_origin_is_not_classified_as_a_violation():
    result = evaluate_lyapunov_sample(np.zeros(2), 0.0)

    assert result.decay_residual == 0.0
    assert not result.derivative_violation
    assert not result.decay_margin_violation


def test_sample_classification_distinguishes_the_two_conditions():
    satisfying = evaluate_lyapunov_sample(np.array([1.0, 0.0]), -1.0)
    margin_only = evaluate_lyapunov_sample(np.array([1.0, 0.0]), -0.01)
    derivative = evaluate_lyapunov_sample(np.array([1.0, 0.0]), 0.01)

    assert not satisfying.derivative_violation
    assert not satisfying.decay_margin_violation
    assert not margin_only.derivative_violation
    assert margin_only.decay_margin_violation
    assert derivative.derivative_violation
    assert derivative.decay_margin_violation


def test_numerical_tolerance_boundary_is_not_the_decay_margin():
    tolerance = 1e-6
    at_boundary = evaluate_lyapunov_sample(
        np.array([1.0, 0.0]),
        tolerance,
        decay_margin=0.0,
        numerical_tolerance=tolerance,
    )
    above_boundary = evaluate_lyapunov_sample(
        np.array([1.0, 0.0]),
        np.nextafter(tolerance, np.inf),
        decay_margin=0.0,
        numerical_tolerance=tolerance,
    )

    assert not at_boundary.derivative_violation
    assert not at_boundary.decay_margin_violation
    assert above_boundary.derivative_violation
    assert above_boundary.decay_margin_violation


def test_zero_decay_margin_makes_both_conditions_equivalent():
    for vdot in (-0.1, 0.1):
        result = evaluate_lyapunov_sample(
            np.array([1.0, 2.0]),
            vdot,
            decay_margin=0.0,
        )
        assert result.decay_residual == pytest.approx(vdot)
        assert result.derivative_violation == result.decay_margin_violation


@pytest.mark.parametrize("decay_margin", [-0.1, np.nan, np.inf])
def test_invalid_decay_margin_is_rejected(decay_margin):
    with pytest.raises(ValueError, match="decay_margin"):
        evaluate_lyapunov_sample(
            np.array([1.0, 0.0]),
            -1.0,
            decay_margin=decay_margin,
        )
    with pytest.raises(ValueError, match="decay_margin"):
        grid_check(lqr_controller, decay_margin=decay_margin)


@pytest.mark.parametrize("numerical_tolerance", [-1e-9, np.nan, np.inf])
def test_invalid_numerical_tolerance_is_rejected(numerical_tolerance):
    with pytest.raises(ValueError, match="numerical_tolerance"):
        evaluate_lyapunov_sample(
            np.array([1.0, 0.0]),
            -1.0,
            numerical_tolerance=numerical_tolerance,
        )


def test_default_grid_excludes_only_the_exact_origin():
    result = grid_check(lqr_controller)

    assert result["sample_count"] == 81 * 81 - 1
    assert result["decay_margin"] == DEFAULT_DECAY_MARGIN
    assert result["numerical_tolerance"] == DEFAULT_NUMERICAL_TOLERANCE
    assert result["derivative_violation_count"] == 0
    assert result["decay_margin_violation_count"] == 0
    assert result["derivative_violation_fraction"] == (
        result["derivative_violation_count"] / result["sample_count"]
    )
    assert result["decay_margin_violation_fraction"] == (
        result["decay_margin_violation_count"] / result["sample_count"]
    )


def test_negative_vdot_does_not_imply_decay_margin_satisfaction():
    """Regression for the weaker historical V-dot-only evaluator."""

    def weakened_lqr_controller(state):
        return float((-0.355 * K @ state.reshape(-1, 1)).item())

    result = grid_check(
        weakened_lqr_controller,
        decay_margin=DEFAULT_DECAY_MARGIN,
    )

    assert result["derivative_violation_fraction"] == 0.0
    assert result["max_vdot"] < 0.0
    assert result["decay_margin_violation_count"] == 224
    assert result["decay_margin_violation_fraction"] > 0.0
    assert result["max_decay_residual"] > 0.0
