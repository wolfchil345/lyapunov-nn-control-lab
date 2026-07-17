from collections.abc import Callable

import numpy as np
import torch
from torch import nn

from src.system import A, B, K, P

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
    margin: float = 0.05,
) -> torch.Tensor:
    """Penalize violations of V-dot <= -margin * ||x||^2."""

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
        margin
        * torch.sum(states**2, dim=1)
    )

    violations = torch.relu(
        v_dot + required_decay
    )

    return violations.mean()


def train_controller(
    model: nn.Module,
    epochs: int = 1000,
    stability_weight: float = 10.0,
    stability_margin: float = 0.05,
) -> dict[str, list[float]]:
    """Train using LQR imitation and a Lyapunov penalty."""

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


def make_nn_controller(
    model: nn.Module,
) -> Callable[[np.ndarray], float]:
    """Convert a PyTorch model into a simulation controller."""

    model.eval()

    def controller(x: np.ndarray) -> float:
        x_tensor = torch.tensor(
            x,
            dtype=torch.float32,
        ).reshape(1, 2)

        with torch.no_grad():
            return float(model(x_tensor).item())

    return controller
