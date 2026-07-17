import numpy as np
import pytest
import torch

from src.controllers import ZeroAtOriginController
from src.lyapunov import grid_check
from src.simulation import simulate
from src.system import A, B, K, lqr_controller


def test_system_matrix_shapes():
    assert A.shape == (2, 2)
    assert B.shape == (2, 1)
    assert K.shape == (1, 2)


def test_lqr_controller_returns_float():
    x = np.array([1.0, 0.0])
    u = lqr_controller(x)

    assert isinstance(u, float)


def test_neural_controller_is_zero_at_origin():
    model = ZeroAtOriginController()
    x = torch.zeros((1, 2))
    u = model(x)

    assert torch.allclose(
        u,
        torch.zeros_like(u),
        atol=1e-6,
    )


def test_lqr_grid_check_has_no_violations():
    result = grid_check(lqr_controller)

    assert result["violation_fraction"] == 0.0
    assert result["maximum_vdot"] < 0.0


@pytest.mark.parametrize(
    "initial_state",
    [
        [1.5, 0.0],
        [-1.5, 0.0],
        [1.0, 1.5],
        [-1.0, -1.5],
        [0.5, -2.0],
    ],
)
def test_lqr_converges_from_multiple_initial_conditions(
    initial_state,
):
    solution = simulate(
        lqr_controller,
        np.array(initial_state, dtype=float),
    )

    final_state_norm = np.linalg.norm(solution.y[:, -1])

    assert solution.success
    assert final_state_norm < 1e-3
