from collections.abc import Callable

import numpy as np
import torch
from torch import nn

from src.system import K

SEED = 7


class ZeroAtOriginController(nn.Module):
    """Neural controller with u(0) = 0."""

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
        return self.net(x) - self.net(zeros)


def make_dataset(n_samples: int = 3000) -> tuple[torch.Tensor, torch.Tensor]:
    """Sample states and label them using the LQR controller."""
    rng = np.random.default_rng(SEED)
    states = rng.uniform(
        low=[-2.0, -3.0],
        high=[2.0, 3.0],
        size=(n_samples, 2),
    ).astype(np.float32)

    actions = (-states @ K.T).astype(np.float32)

    return torch.from_numpy(states), torch.from_numpy(actions)


def train_controller(model: nn.Module, epochs: int = 1000) -> list[float]:
    x_train, u_train = make_dataset()

    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.MSELoss()

    losses: list[float] = []

    model.train()

    for epoch in range(epochs):
        optimizer.zero_grad()

        prediction = model(x_train)
        loss = criterion(prediction, u_train)

        loss.backward()
        optimizer.step()

        losses.append(float(loss.item()))

        if epoch % 100 == 0 or epoch == epochs - 1:
            print(f"epoch={epoch:4d}  mse={loss.item():.6e}")

    return losses


def make_nn_controller(model: nn.Module) -> Callable[[np.ndarray], float]:
    model.eval()

    def controller(x: np.ndarray) -> float:
        x_tensor = torch.tensor(x, dtype=torch.float32).reshape(1, 2)
        with torch.no_grad():
            return float(model(x_tensor).item())

    return controller
