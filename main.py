# lyapunov-nn-control-lab

from __future__ import annotations

import random
from pathlib import Path
from typing import Callable

import control as ct
import matplotlib.pyplot as plt
import numpy as np
import torch
from scipy.integrate import solve_ivp
from torch import nn

SEED = 7
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

# Prevent excessive CPU-thread overhead on some computers.
torch.set_num_threads(1)

# -----------------------------------------------------------------------------
# 1. Plant: mass-spring-damper
#    m*q_ddot + c*q_dot + k*q = u
#    state x = [position, velocity]
# -----------------------------------------------------------------------------
MASS = 1.0
DAMPING = 0.4
STIFFNESS = 2.0

A = np.array(
    [
        [0.0, 1.0],
        [-STIFFNESS / MASS, -DAMPING / MASS],
    ]
)
B = np.array([[0.0], [1.0 / MASS]])

# -----------------------------------------------------------------------------
# 2. Classical baseline: continuous-time LQR
# -----------------------------------------------------------------------------
Q = np.diag([10.0, 1.0])
R = np.array([[0.5]])
K, P, CLOSED_LOOP_EIGENVALUES = ct.lqr(A, B, Q, R)
K = np.asarray(K, dtype=float)
P = np.asarray(P, dtype=float)


def lqr_controller(x: np.ndarray) -> float:
    """Return u = -Kx."""
    return float((-K @ x.reshape(-1, 1)).item())


# -----------------------------------------------------------------------------
# 3. Neural controller
#    Subtracting net(0) guarantees u_nn(0) = 0.
# -----------------------------------------------------------------------------
class ZeroAtOriginController(nn.Module):
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
    """Sample states and label them with the LQR action."""
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


# -----------------------------------------------------------------------------
# 4. Closed-loop simulation
# -----------------------------------------------------------------------------
def simulate(
    controller: Callable[[np.ndarray], float],
    x0: np.ndarray,
    duration: float = 10.0,
):
    def closed_loop_rhs(_t: float, x: np.ndarray) -> np.ndarray:
        u = controller(x)
        return A @ x + B[:, 0] * u

    t_eval = np.linspace(0.0, duration, 1001)
    return solve_ivp(
        closed_loop_rhs,
        (0.0, duration),
        x0,
        t_eval=t_eval,
        rtol=1e-8,
        atol=1e-10,
    )


# -----------------------------------------------------------------------------
# 5. Lyapunov analysis with V(x) = x^T P x
# -----------------------------------------------------------------------------
def lyapunov_value(x: np.ndarray) -> float:
    return float(x.T @ P @ x)


def lyapunov_derivative(
    x: np.ndarray,
    controller: Callable[[np.ndarray], float],
) -> float:
    u = controller(x)
    closed_loop_vector_field = A @ x + B[:, 0] * u
    return float(2.0 * x.T @ P @ closed_loop_vector_field)


def grid_check(controller: Callable[[np.ndarray], float]) -> dict[str, float]:
    """Empirically inspect V-dot on a rectangular state-space grid."""
    positions = np.linspace(-2.0, 2.0, 81)
    velocities = np.linspace(-3.0, 3.0, 81)
    vdots: list[float] = []

    for position in positions:
        for velocity in velocities:
            x = np.array([position, velocity], dtype=float)
            if np.linalg.norm(x) < 1e-9:
                continue
            vdots.append(lyapunov_derivative(x, controller))

    values = np.asarray(vdots)
    return {
        "maximum_vdot": float(values.max()),
        "violation_fraction": float(np.mean(values > 1e-6)),
    }


def save_plots(
    losses: list[float],
    lqr_solution,
    nn_solution,
    output_dir: Path,
) -> None:
    plt.figure(figsize=(8, 5))
    plt.plot(lqr_solution.t, lqr_solution.y[0], label="LQR position")
    plt.plot(nn_solution.t, nn_solution.y[0], "--", label="NN position")
    plt.xlabel("Time [s]")
    plt.ylabel("Position")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "position_comparison.png", dpi=180)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.semilogy(losses)
    plt.xlabel("Epoch")
    plt.ylabel("Training MSE")
    plt.tight_layout()
    plt.savefig(output_dir / "training_loss.png", dpi=180)
    plt.close()


def main() -> None:
    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)

    print("LQR gain K:", K)
    print("Closed-loop eigenvalues:", CLOSED_LOOP_EIGENVALUES)

    model = ZeroAtOriginController()
    losses = train_controller(model)
    nn_controller = make_nn_controller(model)

    initial_state = np.array([1.5, 0.0])
    lqr_solution = simulate(lqr_controller, initial_state)
    nn_solution = simulate(nn_controller, initial_state)

    print("LQR grid check:", grid_check(lqr_controller))
    print("NN grid check:", grid_check(nn_controller))

    torch.save(model.state_dict(), output_dir / "nn_controller.pt")
    save_plots(losses, lqr_solution, nn_solution, output_dir)
    print(f"Saved model and figures in: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
