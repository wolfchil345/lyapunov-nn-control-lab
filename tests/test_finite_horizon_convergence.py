from __future__ import annotations

from types import SimpleNamespace

import numpy as np
import pytest

import lyapunov_nn_control_lab.finite_horizon_convergence as convergence_module
from lyapunov_nn_control_lab.finite_horizon_convergence import (
    MAX_GRID_INITIAL_STATES,
    FiniteHorizonConvergenceResult,
    evaluate_finite_horizon_convergence,
)
from lyapunov_nn_control_lab.region_of_attraction import (
    evaluate_region_of_attraction,
)
from lyapunov_nn_control_lab.system import A, lqr_controller


def zero_controller(_state: np.ndarray) -> float:
    return 0.0


def test_corrected_api_returns_explicit_metadata_and_counts():
    result = evaluate_finite_horizon_convergence(
        lqr_controller,
        position_bounds=(-0.5, 0.5),
        velocity_bounds=(-0.5, 0.5),
        grid_resolution=3,
        convergence_tolerance=1.0,
        horizon=1.0,
        controller_label="LQR",
    )

    assert isinstance(result, FiniteHorizonConvergenceResult)
    assert result.positions.shape == (3,)
    assert result.velocities.shape == (3,)
    assert result.convergence_map.shape == (3, 3)
    assert result.final_norm_map.shape == (3, 3)
    assert result.horizon == 1.0
    assert result.convergence_tolerance == 1.0
    assert result.position_bounds == (-0.5, 0.5)
    assert result.velocity_bounds == (-0.5, 0.5)
    assert result.grid_resolution == 3
    assert result.tested_count == 9
    assert result.converged_count == np.count_nonzero(result.convergence_map)
    assert result.convergence_fraction == pytest.approx(
        result.converged_count / result.tested_count
    )
    assert result.controller_label == "LQR"
    assert result.criterion == "||x(horizon)|| < convergence_tolerance"


def test_grid_and_classification_are_deterministic():
    arguments = {
        "position_bounds": (-0.2, 0.2),
        "velocity_bounds": (-0.4, 0.4),
        "grid_resolution": 3,
        "convergence_tolerance": 0.5,
        "horizon": 0.5,
    }

    first = evaluate_finite_horizon_convergence(lqr_controller, **arguments)
    second = evaluate_finite_horizon_convergence(lqr_controller, **arguments)

    np.testing.assert_array_equal(first.positions, [-0.2, 0.0, 0.2])
    np.testing.assert_array_equal(first.velocities, [-0.4, 0.0, 0.4])
    np.testing.assert_array_equal(first.convergence_map, second.convergence_map)
    np.testing.assert_allclose(first.final_norm_map, second.final_norm_map)


def test_final_state_tolerance_boundary_is_strict(monkeypatch):
    tolerance = 0.25

    def boundary_simulation(_controller, _state, duration):
        return SimpleNamespace(
            success=True,
            t=np.array([0.0, duration]),
            y=np.array([[0.0, tolerance], [0.0, 0.0]]),
        )

    monkeypatch.setattr(convergence_module, "simulate", boundary_simulation)
    result = evaluate_finite_horizon_convergence(
        zero_controller,
        position_bounds=(-1.0, 1.0),
        velocity_bounds=(-1.0, 1.0),
        grid_resolution=2,
        convergence_tolerance=tolerance,
        horizon=1.0,
    )

    assert result.converged_count == 0
    assert not np.any(result.convergence_map)


@pytest.mark.parametrize("horizon", [0.0, -1.0, np.nan, np.inf])
def test_invalid_horizon_is_rejected(horizon):
    with pytest.raises(ValueError, match="horizon"):
        evaluate_finite_horizon_convergence(zero_controller, horizon=horizon)


@pytest.mark.parametrize("tolerance", [0.0, -1.0, np.nan, np.inf])
def test_invalid_convergence_tolerance_is_rejected(tolerance):
    with pytest.raises(ValueError, match="convergence_tolerance"):
        evaluate_finite_horizon_convergence(
            zero_controller,
            convergence_tolerance=tolerance,
        )


@pytest.mark.parametrize(
    ("parameter", "value", "error"),
    [
        ("position_bounds", (1.0, -1.0), ValueError),
        ("position_bounds", (0.0, 0.0), ValueError),
        ("position_bounds", (0.0, np.inf), ValueError),
        ("position_bounds", (0.0,), ValueError),
        ("velocity_bounds", ("low", "high"), TypeError),
        ("grid_resolution", 1, ValueError),
        ("grid_resolution", 2.5, TypeError),
        ("grid_resolution", True, TypeError),
        (
            "grid_resolution",
            int(np.sqrt(MAX_GRID_INITIAL_STATES)) + 1,
            ValueError,
        ),
    ],
)
def test_malformed_grid_inputs_are_rejected(parameter, value, error):
    with pytest.raises(error):
        evaluate_finite_horizon_convergence(
            zero_controller,
            **{parameter: value},
        )


def test_noncallable_controller_is_rejected():
    with pytest.raises(TypeError, match="controller must be callable"):
        evaluate_finite_horizon_convergence(None)  # type: ignore[arg-type]


def test_nonfinite_simulation_trajectory_is_rejected(monkeypatch):
    def nonfinite_simulation(_controller, _state, duration):
        return SimpleNamespace(
            success=True,
            t=np.array([0.0, duration]),
            y=np.array([[0.0, np.nan], [0.0, 0.0]]),
        )

    monkeypatch.setattr(convergence_module, "simulate", nonfinite_simulation)

    with pytest.raises(ValueError, match="finite"):
        evaluate_finite_horizon_convergence(
            zero_controller,
            grid_resolution=2,
        )


def test_failed_simulation_is_not_silently_classified(monkeypatch):
    def failed_simulation(_controller, _state, duration):
        return SimpleNamespace(
            success=False,
            message="solver stopped",
            t=np.array([0.0, duration / 2.0]),
            y=np.zeros((2, 2)),
        )

    monkeypatch.setattr(convergence_module, "simulate", failed_simulation)

    with pytest.raises(RuntimeError, match="solver stopped"):
        evaluate_finite_horizon_convergence(
            zero_controller,
            grid_resolution=2,
        )


def test_nominal_open_loop_matrix_is_hurwitz():
    eigenvalues = np.linalg.eigvals(A)

    assert np.all(np.real(eigenvalues) < 0.0)


def test_hurwitz_open_loop_can_fail_a_short_finite_horizon_criterion():
    eigenvalues = np.linalg.eigvals(A)
    assert np.all(np.real(eigenvalues) < 0.0)

    result = evaluate_finite_horizon_convergence(
        zero_controller,
        position_bounds=(-1.0, 1.0),
        velocity_bounds=(-1.0, 1.0),
        grid_resolution=3,
        convergence_tolerance=0.1,
        horizon=0.1,
        controller_label="Uncontrolled nominal plant",
    )

    assert 0 < result.converged_count < result.tested_count
    assert result.convergence_map[1, 1]
    assert not result.convergence_map[1, 2]


def test_legacy_api_warns_and_returns_legacy_tuple():
    with pytest.warns(DeprecationWarning, match="mathematically misleading"):
        legacy_result = evaluate_region_of_attraction(
            lqr_controller,
            position_range=(-0.1, 0.1),
            velocity_range=(-0.1, 0.1),
            num_points=2,
            convergence_threshold=1.0,
            duration=0.5,
        )

    assert len(legacy_result) == 4
    assert legacy_result[0].shape == (2,)
    assert legacy_result[2].shape == (2, 2)
