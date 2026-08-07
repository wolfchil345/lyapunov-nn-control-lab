import pytest
import torch

from lyapunov_nn_control_lab.controllers import (
    calculate_lyapunov_decay_residuals,
    calculate_lyapunov_penalty,
)
from lyapunov_nn_control_lab.lyapunov import (
    DEFAULT_DECAY_MARGIN,
    evaluate_lyapunov_sample,
    lyapunov_decay_residual,
    lyapunov_derivative,
)
from lyapunov_nn_control_lab.system import A, B, K, P


def test_lqr_actions_have_zero_lyapunov_penalty():
    states = torch.tensor(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [1.0, -1.0],
            [-1.5, 0.5],
        ],
        dtype=torch.float32,
    )

    k_tensor = torch.tensor(
        K,
        dtype=torch.float32,
    )

    lqr_controls = -states @ k_tensor.T

    penalty = calculate_lyapunov_penalty(
        states=states,
        controls=lqr_controls,
        margin=DEFAULT_DECAY_MARGIN,
    )

    assert penalty.item() < 1e-6


def test_training_and_evaluation_use_the_same_decay_residual():
    state = torch.tensor([[-0.35, -3.0]], dtype=torch.float64)
    k_tensor = torch.tensor(K, dtype=torch.float64)
    controls = -0.355 * state @ k_tensor.T

    training_residual = calculate_lyapunov_decay_residuals(
        state,
        controls,
        decay_margin=DEFAULT_DECAY_MARGIN,
    ).item()

    def controller(x):
        return float((-0.355 * K @ x.reshape(-1, 1)).item())

    numpy_state = state.numpy()[0]
    vdot = lyapunov_derivative(numpy_state, controller)
    evaluation_residual = lyapunov_decay_residual(
        numpy_state,
        vdot,
        DEFAULT_DECAY_MARGIN,
    )
    evaluation = evaluate_lyapunov_sample(
        numpy_state,
        vdot,
        decay_margin=DEFAULT_DECAY_MARGIN,
    )

    assert training_residual == pytest.approx(evaluation_residual)
    assert training_residual > 0.0
    assert evaluation.decay_margin_violation


def test_penalty_refactor_preserves_the_existing_training_objective():
    states = torch.tensor(
        [[0.5, -1.0], [-0.25, 2.0], [1.5, 0.75]],
        dtype=torch.float64,
    )
    controls = torch.tensor([[0.2], [-0.4], [0.1]], dtype=torch.float64)
    a_tensor = torch.tensor(A, dtype=torch.float64)
    b_transpose = torch.tensor(B.T, dtype=torch.float64)
    p_tensor = torch.tensor(P, dtype=torch.float64)
    vector_field = states @ a_tensor.T + controls @ b_transpose
    gradient_v = 2.0 * states @ p_tensor
    vdot = torch.sum(gradient_v * vector_field, dim=1)
    expected = torch.relu(
        vdot + DEFAULT_DECAY_MARGIN * torch.sum(states**2, dim=1)
    ).mean()

    actual = calculate_lyapunov_penalty(states, controls)

    assert torch.allclose(actual, expected)
