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
from src.plotting import (
    save_multiple_initial_conditions_plot,
    save_plots,
)
from src.simulation import simulate
from src.system import CLOSED_LOOP_EIGENVALUES, K, lqr_controller

SEED = 7


def set_seed() -> None:
    """Set deterministic random seeds."""

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

    initial_states = [
        np.array([1.5, 0.0]),
        np.array([-1.5, 0.0]),
        np.array([1.0, 1.5]),
        np.array([-1.0, -1.5]),
        np.array([0.5, -2.0]),
    ]

    lqr_solutions = [
        simulate(lqr_controller, initial_state)
        for initial_state in initial_states
    ]

    nn_solutions = [
        simulate(nn_controller, initial_state)
        for initial_state in initial_states
    ]

    all_solutions = lqr_solutions + nn_solutions

    if not all(solution.success for solution in all_solutions):
        raise RuntimeError("At least one simulation failed.")

    print()
    print("Multiple initial-condition results:")

    for initial_state, lqr_solution, nn_solution in zip(
        initial_states,
        lqr_solutions,
        nn_solutions,
    ):
        lqr_final_norm = np.linalg.norm(lqr_solution.y[:, -1])
        nn_final_norm = np.linalg.norm(nn_solution.y[:, -1])

        print(
            f"x0={initial_state}: "
            f"LQR final norm={lqr_final_norm:.6e}, "
            f"NN final norm={nn_final_norm:.6e}"
        )

    print()
    print("LQR grid check:", grid_check(lqr_controller))
    print("NN grid check:", grid_check(nn_controller))

    torch.save(
        model.state_dict(),
        output_dir / "nn_controller.pt",
    )

    # Keep the original one-condition comparison.
    save_plots(
        losses,
        lqr_solutions[0],
        nn_solutions[0],
        output_dir,
    )

    # Add the new multiple-condition experiment.
    save_multiple_initial_conditions_plot(
        nn_solutions,
        initial_states,
        output_dir,
    )

    print()
    print(f"Saved model and figures in: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
