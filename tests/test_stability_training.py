import torch

from src.controllers import (
    calculate_lyapunov_penalty,
)
from src.system import K


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
        margin=0.05,
    )

    assert penalty.item() < 1e-6
