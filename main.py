from pathlib import Path
import random

import numpy as np
import torch

from src.controllers import (
    ZeroAtOriginController,
    make_nn_controller,
    train_controller,
)
from src.lyapunov import grid_check
from src.plotting import save_plots
from src.simulation import simulate
from src.system import CLOSED_LOOP_EIGENVALUES, K, lqr_controller

SEED = 7


def set_seed() -> None:
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)
    torch.set_num_threads(1)


def main() -> None:
    set_seed()

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
