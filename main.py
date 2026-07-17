from pathlib import Path
import csv
import random

import numpy as np
import torch

from src.controllers import (
    ZeroAtOriginController,
    make_nn_controller,
    make_saturated_controller,
    train_controller,
)
from src.lyapunov import grid_check
from src.metrics import calculate_metrics
from src.noise import simulate_with_measurement_noise
from src.plotting import (
    save_multiple_initial_conditions_plot,
    save_plots,
    save_saturation_comparison_plot,
    save_noise_robustness_plot,
)
from src.simulation import simulate
from src.system import (
    CLOSED_LOOP_EIGENVALUES,
    K,
    lqr_controller,
)

SEED = 7
CONTROL_LIMIT = 2.0


def set_seed() -> None:
    """Set deterministic random seeds."""

    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)
    torch.set_num_threads(1)


def save_metrics_csv(
    rows: list[dict[str, float | str]],
    output_path: Path,
) -> None:
    """Save controller metrics as a CSV file."""

    fieldnames = [
        "initial_position",
        "initial_velocity",
        "controller",
        "control_limit",
        "final_state_norm",
        "settling_time_s",
        "quadratic_cost",
        "control_energy",
        "max_abs_control",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    set_seed()

    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)

    print("LQR gain K:", K)
    print("Closed-loop eigenvalues:", CLOSED_LOOP_EIGENVALUES)
    print(f"Actuator saturation limit: +/-{CONTROL_LIMIT}")

    model = ZeroAtOriginController()

    training_history = train_controller(
        model,
        stability_weight=10.0,
        stability_margin=0.05,
    )

    nn_controller = make_nn_controller(model)

    saturated_lqr_controller = make_saturated_controller(
        lqr_controller,
        limit=CONTROL_LIMIT,
    )

    saturated_nn_controller = make_saturated_controller(
        nn_controller,
        limit=CONTROL_LIMIT,
    )

    controllers = {
        "LQR": (lqr_controller, "none"),
        "Neural network": (nn_controller, "none"),
        "Saturated LQR": (saturated_lqr_controller, CONTROL_LIMIT),
        "Saturated neural network": (saturated_nn_controller, CONTROL_LIMIT),
    }

    initial_states = [
        np.array([1.5, 0.0]),
        np.array([-1.5, 0.0]),
        np.array([1.0, 1.5]),
        np.array([-1.0, -1.5]),
        np.array([0.5, -2.0]),
    ]

    solutions: dict[str, list] = {
        controller_name: [
            simulate(controller, initial_state)
            for initial_state in initial_states
        ]
        for controller_name, (controller, _limit) in controllers.items()
    }

    all_solutions = [
        solution
        for controller_solutions in solutions.values()
        for solution in controller_solutions
    ]

    if not all(solution.success for solution in all_solutions):
        raise RuntimeError("At least one simulation failed.")

    metric_rows: list[dict[str, float | str]] = []

    print()
    print("Quantitative performance metrics:")

    for controller_name, (controller, control_limit) in controllers.items():
        for initial_state, solution in zip(
            initial_states,
            solutions[controller_name],
        ):
            metrics = calculate_metrics(solution, controller)

            row = {
                "initial_position": float(initial_state[0]),
                "initial_velocity": float(initial_state[1]),
                "controller": controller_name,
                "control_limit": control_limit,
                **metrics,
            }

            metric_rows.append(row)

            print(
                f"x0={initial_state}, "
                f"{controller_name}: "
                f"settling={metrics['settling_time_s']:.3f} s, "
                f"cost={metrics['quadratic_cost']:.4f}, "
                f"energy={metrics['control_energy']:.4f}, "
                f"max |u|={metrics['max_abs_control']:.4f}, "
                f"final norm={metrics['final_state_norm']:.3e}"
            )

    metrics_path = output_dir / "performance_metrics.csv"
    save_metrics_csv(metric_rows, metrics_path)

    print()
    print("LQR grid check:", grid_check(lqr_controller))
    print("NN grid check:", grid_check(nn_controller))

    torch.save(model.state_dict(), output_dir / "nn_controller.pt")

    save_plots(
        training_history,
        solutions["LQR"][0],
        solutions["Neural network"][0],
        output_dir,
    )

    save_multiple_initial_conditions_plot(
        solutions["Neural network"],
        initial_states,
        output_dir,
    )

    first_initial_condition_solutions = {
        controller_name: controller_solutions[0]
        for controller_name, controller_solutions in solutions.items()
    }

    save_saturation_comparison_plot(
        first_initial_condition_solutions,
        output_dir,
    )

    noise_levels = [0.0, 0.01, 0.05, 0.1]
    noise_initial_state = np.array([1.5, 0.0])

    noise_solutions = {
        noise_std: simulate_with_measurement_noise(
            saturated_nn_controller,
            noise_initial_state,
            noise_std=noise_std,
            seed=SEED + int(noise_std * 1000),
        )
        for noise_std in noise_levels
    }

    if not all(solution.success for solution in noise_solutions.values()):
        raise RuntimeError("At least one noisy simulation failed.")

    print()
    print("Noise robustness results:")

    for noise_std, solution in noise_solutions.items():
        final_norm = np.linalg.norm(solution.y[:, -1])
        print(
            f"noise std={noise_std:g}: "
            f"final norm={final_norm:.3e}"
        )

    save_noise_robustness_plot(
        noise_solutions,
        output_dir,
    )

    print()
    print(f"Metrics saved to: {metrics_path.resolve()}")
    print(f"Model and figures saved in: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
