from pathlib import Path
import csv
import random

import numpy as np
import torch

from src.controllers import (
    ZeroAtOriginController,
    make_nn_controller,
    train_controller,
)
from src.lyapunov import grid_check
from src.metrics import calculate_metrics
from src.plotting import (
    save_multiple_initial_conditions_plot,
    save_plots,
)
from src.simulation import simulate
from src.system import (
    CLOSED_LOOP_EIGENVALUES,
    K,
    lqr_controller,
)

SEED = 7


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
        "final_state_norm",
        "settling_time_s",
        "quadratic_cost",
        "control_energy",
        "max_abs_control",
    ]

    with output_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
        )
        writer.writeheader()
        writer.writerows(rows)


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

    if not all(
        solution.success
        for solution in all_solutions
    ):
        raise RuntimeError(
            "At least one simulation failed."
        )

    metric_rows: list[dict[str, float | str]] = []

    print()
    print("Quantitative performance metrics:")

    for initial_state, lqr_solution, nn_solution in zip(
        initial_states,
        lqr_solutions,
        nn_solutions,
    ):
        controller_cases = [
            (
                "LQR",
                lqr_solution,
                lqr_controller,
            ),
            (
                "Neural network",
                nn_solution,
                nn_controller,
            ),
        ]

        for controller_name, solution, controller in controller_cases:
            metrics = calculate_metrics(
                solution,
                controller,
            )

            row = {
                "initial_position": float(initial_state[0]),
                "initial_velocity": float(initial_state[1]),
                "controller": controller_name,
                **metrics,
            }

            metric_rows.append(row)

            print(
                f"x0={initial_state}, "
                f"{controller_name}: "
                f"settling={metrics['settling_time_s']:.3f} s, "
                f"cost={metrics['quadratic_cost']:.4f}, "
                f"energy={metrics['control_energy']:.4f}, "
                f"final norm={metrics['final_state_norm']:.3e}"
            )

    metrics_path = output_dir / "performance_metrics.csv"
    save_metrics_csv(metric_rows, metrics_path)

    print()
    print("LQR grid check:", grid_check(lqr_controller))
    print("NN grid check:", grid_check(nn_controller))

    torch.save(
        model.state_dict(),
        output_dir / "nn_controller.pt",
    )

    save_plots(
        losses,
        lqr_solutions[0],
        nn_solutions[0],
        output_dir,
    )

    save_multiple_initial_conditions_plot(
        nn_solutions,
        initial_states,
        output_dir,
    )

    print()
    print(f"Metrics saved to: {metrics_path.resolve()}")
    print(
        f"Model and figures saved in: "
        f"{output_dir.resolve()}"
    )


if __name__ == "__main__":
    main()
