from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def save_plots(
    losses: list[float],
    lqr_solution,
    nn_solution,
    output_dir: Path,
) -> None:
    """Save the baseline trajectory and training-loss figures."""

    plt.figure(figsize=(8, 5))
    plt.plot(lqr_solution.t, lqr_solution.y[0], label="LQR position")
    plt.plot(nn_solution.t, nn_solution.y[0], "--", label="NN position")
    plt.xlabel("Time [s]")
    plt.ylabel("Position")
    plt.title("LQR and neural-controller comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_dir / "position_comparison.png", dpi=180)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.semilogy(losses)
    plt.xlabel("Epoch")
    plt.ylabel("Training MSE")
    plt.title("Neural-controller training loss")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_dir / "training_loss.png", dpi=180)
    plt.close()


def save_multiple_initial_conditions_plot(
    nn_solutions: list,
    initial_states: list[np.ndarray],
    output_dir: Path,
) -> None:
    """Plot the NN-controlled state norm for several initial conditions."""

    plt.figure(figsize=(9, 6))

    for initial_state, solution in zip(initial_states, nn_solutions):
        state_norm = np.linalg.norm(solution.y, axis=0)

        # Avoid log(0) when the trajectory becomes extremely small.
        state_norm = np.maximum(state_norm, 1e-12)

        label = (
            f"x0 = [{initial_state[0]:.1f}, "
            f"{initial_state[1]:.1f}]"
        )

        plt.semilogy(solution.t, state_norm, label=label)

    plt.xlabel("Time [s]")
    plt.ylabel("State norm ||x||")
    plt.title("NN controller from multiple initial conditions")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(
        output_dir / "multiple_initial_conditions.png",
        dpi=180,
    )
    plt.close()
