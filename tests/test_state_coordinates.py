from __future__ import annotations

import inspect
from types import SimpleNamespace

import numpy as np
import pytest
import torch

import lyapunov_nn_control_lab.finite_horizon_convergence as convergence_module
import lyapunov_nn_control_lab.metrics as metrics_module
import lyapunov_nn_control_lab.plotting as plotting_module
import lyapunov_nn_control_lab.reporting as reporting_module
from lyapunov_nn_control_lab.controllers import (
    calculate_lyapunov_decay_residuals,
)
from lyapunov_nn_control_lab.finite_horizon_convergence import (
    evaluate_finite_horizon_convergence,
)
from lyapunov_nn_control_lab.lyapunov import lyapunov_decay_residual
from lyapunov_nn_control_lab.metrics import calculate_metrics
from lyapunov_nn_control_lab.noise import add_measurement_noise
from lyapunov_nn_control_lab.simulation import simulate
from lyapunov_nn_control_lab.state_coordinates import (
    NORMALIZED_POSITION_LABEL,
    NORMALIZED_STATE_CONVENTION,
    NORMALIZED_STATE_NORM_LABEL,
    NORMALIZED_TIME_LABEL,
    NORMALIZED_VELOCITY_LABEL,
    squared_state_norm,
    state_norm,
    torch_squared_state_norm,
    torch_state_norm,
)
from lyapunov_nn_control_lab.system import (
    A,
    B,
    K,
    LQR_COST_CONVENTION,
    P,
    Q,
    R,
    SYSTEM_PARAMETER_CONVENTION,
    lqr_controller,
)


def zero_controller(_state: np.ndarray) -> float:
    return 0.0


def test_normalized_coordinate_metadata_is_explicit():
    convention = NORMALIZED_STATE_CONVENTION

    assert convention.dimensionless
    assert convention.time_symbol == "tau"
    assert convention.position_symbol == "q"
    assert convention.velocity_symbol == "v = dq/dtau"
    assert convention.control_symbol == "u"
    assert "normalized" in SYSTEM_PARAMETER_CONVENTION
    assert "normalized time" in LQR_COST_CONVENTION


def test_state_norm_and_squared_norm_are_euclidean():
    state = np.array([3.0, 4.0])

    assert squared_state_norm(state) == 25.0
    assert state_norm(state) == 5.0


@pytest.mark.parametrize(
    ("state", "error"),
    [
        ([1.0], ValueError),
        ([[1.0, 2.0]], ValueError),
        ([1.0, np.nan], ValueError),
        ("1, 2", TypeError),
    ],
)
def test_state_magnitude_helpers_reuse_state_validation(state, error):
    with pytest.raises(error):
        state_norm(state)
    with pytest.raises(error):
        squared_state_norm(state)


def test_numpy_and_torch_state_magnitudes_match_and_remain_differentiable():
    values = np.array([[3.0, 4.0], [-1.5, 2.0]], dtype=np.float64)
    states = torch.tensor(values, dtype=torch.float64, requires_grad=True)

    torch_squared = torch_squared_state_norm(states)
    torch_norms = torch_state_norm(states)

    np.testing.assert_allclose(
        torch_squared.detach().numpy(),
        [squared_state_norm(state) for state in values],
    )
    np.testing.assert_allclose(
        torch_norms.detach().numpy(),
        [state_norm(state) for state in values],
    )
    torch_squared.sum().backward()
    torch.testing.assert_close(states.grad, 2.0 * states.detach())


def test_lyapunov_training_and_evaluation_share_squared_state_magnitude():
    state = np.array([0.75, -1.25], dtype=np.float64)
    states = torch.tensor(state[np.newaxis, :], dtype=torch.float64)
    controls = torch.tensor([[0.2]], dtype=torch.float64)
    decay_margin = 0.05

    vector_field = states @ torch.tensor(A).T + controls @ torch.tensor(B.T)
    gradient_v = 2.0 * states @ torch.tensor(P)
    vdot = torch.sum(gradient_v * vector_field, dim=1).item()
    training_residual = calculate_lyapunov_decay_residuals(
        states,
        controls,
        decay_margin=decay_margin,
    ).item()
    evaluation_residual = lyapunov_decay_residual(
        state,
        vdot,
        decay_margin,
    )

    expected = vdot + decay_margin * squared_state_norm(state)
    assert training_residual == pytest.approx(expected)
    assert evaluation_residual == pytest.approx(expected)


def test_finite_horizon_evaluator_uses_shared_state_norm(monkeypatch):
    calls: list[np.ndarray] = []

    def fake_simulate(_controller, _state, duration):
        return SimpleNamespace(
            success=True,
            message="ok",
            t=np.array([0.0, duration]),
            y=np.array([[0.0, 0.3], [0.0, 0.4]]),
        )

    def recording_norm(state):
        calls.append(np.asarray(state).copy())
        return state_norm(state)

    monkeypatch.setattr(convergence_module, "simulate", fake_simulate)
    monkeypatch.setattr(convergence_module, "state_norm", recording_norm)

    result = evaluate_finite_horizon_convergence(
        zero_controller,
        grid_resolution=2,
        convergence_tolerance=0.6,
        horizon=1.0,
    )

    assert len(calls) == 4
    assert np.all(result.final_norm_map == 0.5)
    assert np.all(result.convergence_map)


def test_metrics_use_shared_norm_and_remains_inside_settling_semantics(
    monkeypatch,
):
    time = np.arange(5.0)
    states = np.array(
        [[0.03, 0.01, 0.03, 0.02, 0.01], [0.0, 0.0, 0.0, 0.0, 0.0]]
    )
    solution = SimpleNamespace(success=True, t=time, y=states)
    calls: list[np.ndarray] = []

    def recording_norm(state):
        calls.append(np.asarray(state).copy())
        return state_norm(state)

    monkeypatch.setattr(metrics_module, "state_norm", recording_norm)
    metrics = calculate_metrics(
        solution,
        zero_controller,
        settling_threshold=0.02,
    )

    assert len(calls) == len(time)
    assert metrics["settling_time"] == 3.0
    assert metrics["settling_time_s"] == metrics["settling_time"]
    assert metrics["final_state_norm"] == 0.01
    assert metrics["integrated_squared_control_effort"] == 0.0
    assert metrics["control_energy"] == 0.0


def test_noise_is_independent_in_both_normalized_coordinates():
    state = np.array([0.5, -0.25])
    actual_rng = np.random.default_rng(19)
    expected_rng = np.random.default_rng(19)

    actual = add_measurement_noise(state, noise_std=0.1, rng=actual_rng)
    expected = state + expected_rng.normal(0.0, 0.1, size=(2,))

    np.testing.assert_array_equal(actual, expected)
    doc = inspect.getdoc(add_measurement_noise)
    assert doc is not None
    assert "independent Gaussian noise" in doc
    assert "normalized state coordinates" in doc


def test_future_plot_and_report_labels_do_not_claim_si_units():
    assert NORMALIZED_TIME_LABEL == "Normalized time"
    assert NORMALIZED_POSITION_LABEL.startswith("Normalized position")
    assert NORMALIZED_VELOCITY_LABEL.startswith("Normalized velocity")
    assert NORMALIZED_STATE_NORM_LABEL.startswith("Normalized state norm")

    generator_source = inspect.getsource(plotting_module)
    report_source = inspect.getsource(reporting_module)
    for unsupported_label in ("Time [s]", "Horizon [s]", "Control energy"):
        assert unsupported_label not in generator_source
        assert unsupported_label not in report_source


def test_system_matrices_and_quick_start_metrics_are_numerically_unchanged():
    np.testing.assert_array_equal(A, [[0.0, 1.0], [-2.0, -0.4]])
    np.testing.assert_array_equal(B, [[0.0], [1.0]])
    np.testing.assert_array_equal(Q, [[10.0, 0.0], [0.0, 1.0]])
    np.testing.assert_array_equal(R, [[0.5]])
    np.testing.assert_allclose(
        K,
        [[2.898979485566353, 2.4209854609927888]],
        rtol=0.0,
        atol=1e-14,
    )
    np.testing.assert_allclose(
        P,
        [
            [6.509974951242312, 1.4494897427831765],
            [1.4494897427831765, 1.2104927304963944],
        ],
        rtol=0.0,
        atol=1e-14,
    )

    solution = simulate(lqr_controller, np.array([1.0, 0.0]), duration=5.0)
    metrics = calculate_metrics(solution, lqr_controller)

    assert metrics["final_state_norm"] == pytest.approx(
        0.0019408257736353866,
        rel=0.0,
        abs=1e-15,
    )
    assert metrics["settling_time"] == 3.25
    assert metrics["quadratic_cost"] == pytest.approx(
        6.510042136552034,
        rel=0.0,
        abs=1e-12,
    )
    assert metrics["integrated_squared_control_effort"] == pytest.approx(
        metrics["control_energy"]
    )
