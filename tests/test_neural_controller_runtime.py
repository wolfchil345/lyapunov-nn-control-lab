from __future__ import annotations

import numpy as np
import pytest
import torch
from torch import nn

from lyapunov_nn_control_lab.controllers import make_nn_controller


class RecordingModel(nn.Module):
    def __init__(self, *, dtype: torch.dtype, device: torch.device) -> None:
        super().__init__()
        self.weight = nn.Parameter(
            torch.tensor([[2.0, -1.0]], dtype=dtype, device=device)
        )
        self.seen_dtype: torch.dtype | None = None
        self.seen_device: torch.device | None = None
        self.grad_enabled: bool | None = None

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        self.seen_dtype = inputs.dtype
        self.seen_device = inputs.device
        self.grad_enabled = torch.is_grad_enabled()
        return inputs @ self.weight.T


@pytest.mark.parametrize("dtype", [torch.float32, torch.float64])
def test_neural_controller_infers_model_dtype_and_disables_gradients(dtype):
    model = RecordingModel(dtype=dtype, device=torch.device("cpu"))
    model.train()
    controller = make_nn_controller(model)

    output = controller(np.array([0.75, -0.25]))

    assert output == pytest.approx(1.75)
    assert model.seen_dtype == dtype
    assert model.seen_device == torch.device("cpu")
    assert model.grad_enabled is False
    assert model.training is True


@pytest.mark.skipif(not torch.cuda.is_available(), reason="CUDA is unavailable")
def test_neural_controller_infers_cuda_device():
    device = torch.device("cuda")
    model = RecordingModel(dtype=torch.float32, device=device)
    controller = make_nn_controller(model)

    assert controller(np.array([0.75, -0.25])) == pytest.approx(1.75)
    assert model.seen_device == device


def test_neural_controller_supports_parameterless_model():
    class ParameterlessModel(nn.Module):
        def forward(self, inputs: torch.Tensor) -> torch.Tensor:
            return inputs.sum().reshape(1, 1)

    controller = make_nn_controller(ParameterlessModel())

    assert controller(np.array([1.0, 2.0])) == pytest.approx(3.0)


def test_neural_controller_rejects_malformed_output_shape():
    class MalformedModel(nn.Module):
        def forward(self, inputs: torch.Tensor) -> torch.Tensor:
            return torch.cat([inputs, inputs], dim=1)

    controller = make_nn_controller(MalformedModel())

    with pytest.raises(ValueError, match="exactly one value"):
        controller(np.array([1.0, 2.0]))


@pytest.mark.parametrize("value", [float("nan"), float("inf"), -float("inf")])
def test_neural_controller_rejects_nonfinite_output(value):
    class NonfiniteModel(nn.Module):
        def forward(self, inputs: torch.Tensor) -> torch.Tensor:
            return torch.full((1, 1), value, device=inputs.device)

    controller = make_nn_controller(NonfiniteModel())

    with pytest.raises(ValueError, match="must be finite"):
        controller(np.array([1.0, 2.0]))
