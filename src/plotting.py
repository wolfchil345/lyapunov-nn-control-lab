from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def save_plots(
    training_history: dict[str, list[float]],
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
    plt.title("LQR and neural-controller comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_dir / "position_comparison.png", dpi=180)
    plt.close()

    plt.figure(figsize=(8, 5))

    loss_labels = {
        "total": "Total loss",
        "imitation": "Imitation loss",
        "stability": "Lyapunov penalty",
    }

    for key, label in loss_labels.items():
        values = np.asarray(training_history[key], dtype=float)
        values = np.maximum(values, 1e-12)
        plt.semilogy(values, label=label)

    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Stability-aware controller training")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_dir / "training_loss.png", dpi=180)
    plt.close()


def save_multiple_initial_conditions_plot(
    nn_solutions: list,
    initial_states: list[np.ndarray],
    output_dir: Path,
) -> None:
    """Plot NN state norms for multiple initial conditions."""

    plt.figure(figsize=(9, 6))

    for initial_state, solution in zip(initial_states, nn_solutions):
        state_norm = np.linalg.norm(solution.y, axis=0)
        state_norm = np.maximum(state_norm, 1e-12)

        label = f"x0 = [{initial_state[0]:.1f}, {initial_state[1]:.1f}]"
        plt.semilogy(solution.t, state_norm, label=label)

    plt.xlabel("Time [s]")
    plt.ylabel("State norm ||x||")
    plt.title("NN controller from multiple initial conditions")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "multiple_initial_conditions.png", dpi=180)
    plt.close()


def save_saturation_comparison_plot(
    solutions_by_controller: dict[str, object],
    output_dir: Path,
) -> None:
    """Compare state norms for saturated and unsaturated controllers."""

    plt.figure(figsize=(9, 6))

    for controller_name, solution in solutions_by_controller.items():
        state_norm = np.linalg.norm(solution.y, axis=0)
        state_norm = np.maximum(state_norm, 1e-12)

        plt.semilogy(
            solution.t,
            state_norm,
            label=controller_name,
        )

    plt.xlabel("Time [s]")
    plt.ylabel("State norm ||x||")
    plt.title("Effect of actuator saturation")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "saturation_comparison.png", dpi=180)
    plt.close()


def save_noise_robustness_plot(
    noise_solutions_by_std: dict[float, object],
    output_dir: Path,
) -> None:
    """Compare trajectories under different measurement-noise levels."""

    plt.figure(figsize=(9, 6))

    for noise_std, solution in noise_solutions_by_std.items():
        state_norm = np.linalg.norm(solution.y, axis=0)
        state_norm = np.maximum(state_norm, 1e-12)

        plt.semilogy(
            solution.t,
            state_norm,
            label=f"noise std = {noise_std:g}",
        )

    plt.xlabel("Time [s]")
    plt.ylabel("State norm ||x||")
    plt.title("Noise robustness of saturated NN controller")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "noise_robustness.png", dpi=180)
    plt.close()


def save_parameter_robustness_plot(
    parameter_solutions: dict[str, object],
    output_dir: Path,
) -> None:
    """Compare trajectories under plant-parameter variations."""

    plt.figure(figsize=(9, 6))

    for scenario_name, solution in parameter_solutions.items():
        state_norm = np.linalg.norm(solution.y, axis=0)
        state_norm = np.maximum(state_norm, 1e-12)

        plt.semilogy(
            solution.t,
            state_norm,
            label=scenario_name,
        )

    plt.xlabel("Time [s]")
    plt.ylabel("State norm ||x||")
    plt.title("Parameter robustness of saturated NN controller")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "parameter_robustness.png", dpi=180)
    plt.close()
