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


def save_phase_portrait_plot(
    nn_solutions: list,
    initial_states: list[np.ndarray],
    output_dir: Path,
) -> None:
    """Plot NN closed-loop trajectories in phase space."""

    plt.figure(figsize=(7, 7))

    for initial_state, solution in zip(initial_states, nn_solutions):
        plt.plot(
            solution.y[0],
            solution.y[1],
            label=f"x0 = [{initial_state[0]:.1f}, {initial_state[1]:.1f}]",
        )
        plt.scatter(
            solution.y[0, 0],
            solution.y[1, 0],
            marker="o",
            s=30,
        )

    plt.scatter(
        0.0,
        0.0,
        marker="x",
        s=80,
        label="equilibrium",
    )

    plt.xlabel("Position")
    plt.ylabel("Velocity")
    plt.title("Phase portrait of NN closed-loop trajectories")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig(output_dir / "phase_portrait.png", dpi=180)
    plt.close()


def save_lyapunov_contour_plot(
    nn_solutions: list,
    initial_states: list[np.ndarray],
    lyapunov_matrix: np.ndarray,
    output_dir: Path,
) -> None:
    """Plot Lyapunov level sets with NN closed-loop trajectories."""

    position_values = np.linspace(-2.5, 2.5, 200)
    velocity_values = np.linspace(-2.5, 2.5, 200)

    position_grid, velocity_grid = np.meshgrid(
        position_values,
        velocity_values,
    )

    lyapunov_values = (
        lyapunov_matrix[0, 0] * position_grid**2
        + (lyapunov_matrix[0, 1] + lyapunov_matrix[1, 0])
        * position_grid
        * velocity_grid
        + lyapunov_matrix[1, 1] * velocity_grid**2
    )

    plt.figure(figsize=(8, 7))

    contour = plt.contour(
        position_grid,
        velocity_grid,
        lyapunov_values,
        levels=15,
    )
    plt.clabel(contour, inline=True, fontsize=8)

    for initial_state, solution in zip(initial_states, nn_solutions):
        plt.plot(
            solution.y[0],
            solution.y[1],
            label=f"x0 = [{initial_state[0]:.1f}, {initial_state[1]:.1f}]",
        )
        plt.scatter(
            solution.y[0, 0],
            solution.y[1, 0],
            marker="o",
            s=25,
        )

    plt.scatter(
        0.0,
        0.0,
        marker="x",
        s=90,
        label="equilibrium",
    )

    plt.xlabel("Position")
    plt.ylabel("Velocity")
    plt.title("Lyapunov contours and NN closed-loop trajectories")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig(output_dir / "lyapunov_contours.png", dpi=180)
    plt.close()


def save_region_of_attraction_plot(
    positions: np.ndarray,
    velocities: np.ndarray,
    convergence_map: np.ndarray,
    final_norm_map: np.ndarray,
    output_dir: Path,
) -> None:
    """Plot estimated region of attraction for a controller."""

    plt.figure(figsize=(8, 7))

    image = plt.imshow(
        convergence_map.astype(float),
        origin="lower",
        extent=[
            positions[0],
            positions[-1],
            velocities[0],
            velocities[-1],
        ],
        aspect="auto",
        interpolation="nearest",
    )

    colorbar = plt.colorbar(image, ticks=[0.0, 1.0])
    colorbar.ax.set_yticklabels(
        [
            "not converged",
            "converged",
        ],
    )

    plt.contour(
        positions,
        velocities,
        final_norm_map,
        levels=8,
    )

    plt.scatter(
        0.0,
        0.0,
        marker="x",
        s=90,
        label="equilibrium",
    )

    plt.xlabel("Initial position")
    plt.ylabel("Initial velocity")
    plt.title("Estimated region of attraction")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "region_of_attraction.png", dpi=180)
    plt.close()


def save_stability_weight_ablation_plot(
    rows: list[dict[str, float]],
    output_dir: Path,
) -> None:
    """Plot stability metrics for different Lyapunov penalty weights."""

    x_values = np.arange(len(rows))
    labels = [
        f"{float(row['stability_weight']):g}"
        for row in rows
    ]

    violation_fraction = np.maximum(
        [row["lyapunov_violation_fraction"] for row in rows],
        1e-12,
    )
    final_state_norm = np.maximum(
        [row["final_state_norm"] for row in rows],
        1e-12,
    )
    control_energy = np.maximum(
        [row["control_energy"] for row in rows],
        1e-12,
    )

    plt.figure(figsize=(9, 6))
    plt.semilogy(
        x_values,
        violation_fraction,
        marker="o",
        label="Lyapunov violation fraction",
    )
    plt.semilogy(
        x_values,
        final_state_norm,
        marker="s",
        label="Final state norm",
    )
    plt.semilogy(
        x_values,
        control_energy,
        marker="^",
        label="Control energy",
    )

    plt.xticks(x_values, labels)
    plt.xlabel("Stability weight")
    plt.ylabel("Metric value")
    plt.title("Stability-weight ablation study")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "stability_weight_ablation.png", dpi=180)
    plt.close()


def save_region_of_attraction_comparison_plot(
    comparison_results: dict[str, tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]],
    output_dir: Path,
) -> None:
    """Compare estimated regions of attraction for multiple controllers."""

    num_controllers = len(comparison_results)

    fig, axes = plt.subplots(
        1,
        num_controllers,
        figsize=(5 * num_controllers, 5),
        squeeze=False,
    )

    for axis, (controller_name, result) in zip(
        axes[0],
        comparison_results.items(),
    ):
        positions, velocities, convergence_map, final_norm_map = result

        image = axis.imshow(
            convergence_map.astype(float),
            origin="lower",
            extent=[
                positions[0],
                positions[-1],
                velocities[0],
                velocities[-1],
            ],
            aspect="auto",
            interpolation="nearest",
        )

        axis.contour(
            positions,
            velocities,
            final_norm_map,
            levels=8,
        )

        axis.scatter(
            0.0,
            0.0,
            marker="x",
            s=80,
            label="equilibrium",
        )

        convergence_rate = 100.0 * np.mean(convergence_map)

        axis.set_title(
            f"{controller_name}\nconverged: {convergence_rate:.1f}%"
        )
        axis.set_xlabel("Initial position")
        axis.set_ylabel("Initial velocity")
        axis.grid(True)
        axis.legend()

    colorbar = fig.colorbar(
        image,
        ax=axes.ravel().tolist(),
        ticks=[0.0, 1.0],
        shrink=0.85,
    )
    colorbar.ax.set_yticklabels(
        [
            "not converged",
            "converged",
        ],
    )

    fig.suptitle("Region of attraction comparison")
    fig.subplots_adjust(wspace=0.35, top=0.82, right=0.90)
    fig.savefig(output_dir / "region_of_attraction_comparison.png", dpi=180)
    plt.close(fig)


def save_model_architecture_diagram(output_dir: Path) -> None:
    """Save a simple block diagram of the neural-network control loop."""

    fig, axis = plt.subplots(figsize=(11, 4))
    axis.axis("off")

    nodes = [
        ("State\nx = [position, velocity]", 0.10, 0.55),
        ("Neural-network\ncontroller", 0.34, 0.55),
        ("Control input\nu", 0.55, 0.55),
        ("Mass-spring-damper\nplant", 0.76, 0.55),
        ("Next state\nx(t + dt)", 0.95, 0.55),
    ]

    for label, x_position, y_position in nodes:
        axis.text(
            x_position,
            y_position,
            label,
            ha="center",
            va="center",
            fontsize=11,
            bbox={
                "boxstyle": "round,pad=0.45",
                "linewidth": 1.5,
                "facecolor": "white",
            },
        )

    arrow_pairs = [
        (nodes[0], nodes[1]),
        (nodes[1], nodes[2]),
        (nodes[2], nodes[3]),
        (nodes[3], nodes[4]),
    ]

    for start_node, end_node in arrow_pairs:
        _start_label, start_x, start_y = start_node
        _end_label, end_x, end_y = end_node

        axis.annotate(
            "",
            xy=(end_x - 0.08, end_y),
            xytext=(start_x + 0.08, start_y),
            arrowprops={
                "arrowstyle": "->",
                "linewidth": 1.8,
            },
        )

    axis.annotate(
        "feedback",
        xy=(0.12, 0.35),
        xytext=(0.88, 0.35),
        ha="center",
        va="center",
        arrowprops={
            "arrowstyle": "->",
            "linewidth": 1.4,
            "connectionstyle": "arc3,rad=-0.25",
        },
    )

    axis.text(
        0.5,
        0.88,
        "Closed-loop neural-network control architecture",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
    )

    fig.tight_layout()
    fig.savefig(output_dir / "model_architecture.png", dpi=180)
    plt.close(fig)
