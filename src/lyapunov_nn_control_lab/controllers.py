from collections.abc import Callable
from itertools import chain
from numbers import Integral

import numpy as np
import torch
from torch import nn

from .lyapunov import DEFAULT_DECAY_MARGIN
from .system import A, B, K, P
from ._validation import (
    evaluate_controller,
    validate_finite_scalar,
    validate_nonnegative_scalar,
    validate_positive_scalar,
    validate_state,
)

SEED = 7


class ZeroAtOriginController(nn.Module):
    """Neural controller constrained so that u(0) = 0."""

    def __init__(self) -> None:
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(2, 32),
            nn.Tanh(),
            nn.Linear(32, 32),
            nn.Tanh(),
            nn.Linear(32, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        zeros = torch.zeros_like(x)

        # Enforce the equilibrium condition u(0) = 0.
        return self.net(x) - self.net(zeros)


def make_dataset(
    n_samples: int = 3000,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Generate states and corresponding LQR control targets."""

    if isinstance(n_samples, bool) or not isinstance(n_samples, Integral):
        raise TypeError("n_samples must be a positive integer.")
    if n_samples <= 0:
        raise ValueError("n_samples must be a positive integer.")

    rng = np.random.default_rng(SEED)

    states = rng.uniform(
        low=[-2.0, -3.0],
        high=[2.0, 3.0],
        size=(n_samples, 2),
    ).astype(np.float32)

    actions = (-states @ K.T).astype(np.float32)

    return (
        torch.from_numpy(states),
        torch.from_numpy(actions),
    )


def calculate_lyapunov_penalty(
    states: torch.Tensor,
    controls: torch.Tensor,
    margin: float = DEFAULT_DECAY_MARGIN,
) -> torch.Tensor:
    """Penalize violations of V-dot <= -margin * ||x||^2."""

    residuals = calculate_lyapunov_decay_residuals(
        states,
        controls,
        decay_margin=margin,
    )
    return torch.relu(residuals).mean()


def calculate_lyapunov_decay_residuals(
    states: torch.Tensor,
    controls: torch.Tensor,
    decay_margin: float = DEFAULT_DECAY_MARGIN,
) -> torch.Tensor:
    """Return V-dot + decay_margin * ||x||^2 for training samples."""

    decay_margin = validate_nonnegative_scalar(
        decay_margin,
        name="decay_margin",
    )

    dtype = states.dtype
    device = states.device

    a_tensor = torch.as_tensor(
        A,
        dtype=dtype,
        device=device,
    )

    b_transpose = torch.as_tensor(
        B.T,
        dtype=dtype,
        device=device,
    )

    p_tensor = torch.as_tensor(
        P,
        dtype=dtype,
        device=device,
    )

    # Closed-loop vector field:
    # f(x) = A x + B u
    vector_field = (
        states @ a_tensor.T
        + controls @ b_transpose
    )

    # For V(x) = x^T P x:
    # grad V = 2 P x
    gradient_v = 2.0 * states @ p_tensor

    v_dot = torch.sum(
        gradient_v * vector_field,
        dim=1,
    )

    required_decay = (
        decay_margin
        * torch.sum(states**2, dim=1)
    )

    return v_dot + required_decay


def train_controller(
    model: nn.Module,
    epochs: int = 1000,
    stability_weight: float = 10.0,
    stability_margin: float = DEFAULT_DECAY_MARGIN,
) -> dict[str, list[float]]:
    """Train using LQR imitation and a Lyapunov penalty."""

    if isinstance(epochs, bool) or not isinstance(epochs, Integral):
        raise TypeError("epochs must be a positive integer.")
    if epochs <= 0:
        raise ValueError("epochs must be a positive integer.")
    stability_weight = validate_nonnegative_scalar(
        stability_weight,
        name="stability_weight",
    )
    stability_margin = validate_nonnegative_scalar(
        stability_margin,
        name="stability_margin",
    )

    x_train, u_train = make_dataset()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=1e-3,
    )

    mse_criterion = nn.MSELoss()

    history: dict[str, list[float]] = {
        "total": [],
        "imitation": [],
        "stability": [],
    }

    model.train()

    for epoch in range(epochs):
        optimizer.zero_grad()

        prediction = model(x_train)

        imitation_loss = mse_criterion(
            prediction,
            u_train,
        )

        stability_loss = calculate_lyapunov_penalty(
            states=x_train,
            controls=prediction,
            margin=stability_margin,
        )

        total_loss = (
            imitation_loss
            + stability_weight * stability_loss
        )

        total_loss.backward()
        optimizer.step()

        history["total"].append(
            float(total_loss.item())
        )

        history["imitation"].append(
            float(imitation_loss.item())
        )

        history["stability"].append(
            float(stability_loss.item())
        )

        if epoch % 100 == 0 or epoch == epochs - 1:
            print(
                f"epoch={epoch:4d}  "
                f"total={total_loss.item():.6e}  "
                f"imitation={imitation_loss.item():.6e}  "
                f"stability={stability_loss.item():.6e}"
            )

    return history



DEFAULT_CONTROL_LIMIT = 5.0


def saturate_control(
    control: float,
    limit: float = DEFAULT_CONTROL_LIMIT,
) -> float:
    """Clip the control input to actuator limits."""

    control = validate_finite_scalar(control, name="control")
    limit = validate_positive_scalar(limit, name="control limit")
    return float(np.clip(control, -limit, limit))


def make_saturated_controller(
    controller: Callable[[np.ndarray], float],
    limit: float = DEFAULT_CONTROL_LIMIT,
) -> Callable[[np.ndarray], float]:
    """Wrap a controller with actuator saturation."""

    if not callable(controller):
        raise TypeError("controller must be callable.")
    limit = validate_positive_scalar(limit, name="control limit")

    def saturated_controller(x: np.ndarray) -> float:
        state = validate_state(x, name="controller state")
        raw_control = evaluate_controller(controller, state)
        return saturate_control(raw_control, limit)

    return saturated_controller

def _model_dtype_and_device(model: nn.Module) -> tuple[torch.dtype, torch.device]:
    """Infer floating dtype and device from model parameters or buffers."""

    first_device: torch.device | None = None
    for tensor in chain(model.parameters(), model.buffers()):
        if first_device is None:
            first_device = tensor.device
        if tensor.is_floating_point():
            return tensor.dtype, tensor.device

    return torch.get_default_dtype(), first_device or torch.device("cpu")


def make_nn_controller(
    model: nn.Module,
) -> Callable[[np.ndarray], float]:
    """Convert a PyTorch model into a simulation controller."""

    if not isinstance(model, nn.Module):
        raise TypeError("model must be a torch.nn.Module.")

    def controller(x: np.ndarray) -> float:
        state = validate_state(x, name="controller state")
        dtype, device = _model_dtype_and_device(model)
        x_tensor = torch.as_tensor(
            state,
            dtype=dtype,
            device=device,
        ).reshape(1, 2)

        module_modes = [(module, module.training) for module in model.modules()]
        try:
            model.eval()
            with torch.inference_mode():
                output = model(x_tensor)
        finally:
            for module, was_training in module_modes:
                module.training = was_training

        if not isinstance(output, torch.Tensor):
            raise TypeError("Neural controller output must be a tensor.")
        if output.numel() != 1:
            raise ValueError(
                "Neural controller output must contain exactly one value; "
                f"received shape {tuple(output.shape)}."
            )
        if not bool(torch.isfinite(output).all().item()):
            raise ValueError("Neural controller output must be finite.")
        return float(output.item())

    return controller
