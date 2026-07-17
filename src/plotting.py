from pathlib import Path

import matplotlib.pyplot as plt


def save_plots(
    losses: list[float],
    lqr_solution,
    nn_solution,
    output_dir: Path,
) -> None:
    """Save trajectory and training-loss figures."""
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
