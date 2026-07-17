import csv
import random
from pathlib import Path
from typing import Any

import numpy as np
import torch

from src.controllers import (
    ZeroAtOriginController,
    make_nn_controller,
    train_controller,
)
from src.lyapunov import grid_check
from src.metrics import calculate_metrics
from src.simulation import simulate


def set_ablation_seed(seed: int) -> None:
    """Set random seeds for repeatable ablation runs."""

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.set_num_threads(1)


def get_metric(
    result: dict[str, Any],
    possible_keys: list[str],
) -> float:
    """Get a metric from a dictionary using several possible key names."""

    for key in possible_keys:
        if key in result:
            return float(result[key])

    raise KeyError(
        "None of these keys were found: "
        f"{possible_keys}. Available keys: {list(result.keys())}"
    )


def run_stability_weight_ablation(
    stability_weights: list[float],
    initial_state: np.ndarray,
    epochs: int = 300,
    stability_margin: float = 0.05,
    base_seed: int = 700,
) -> list[dict[str, float]]:
    """Train controllers with different Lyapunov penalty weights."""

    rows: list[dict[str, float]] = []

    for index, stability_weight in enumerate(stability_weights):
        set_ablation_seed(base_seed + index)

        model = ZeroAtOriginController()
        history = train_controller(
            model,
            epochs=epochs,
            stability_weight=stability_weight,
            stability_margin=stability_margin,
        )

        controller = make_nn_controller(model)
        solution = simulate(controller, initial_state)

        if not solution.success:
            raise RuntimeError(
                f"Simulation failed for stability_weight={stability_weight}."
            )

        metrics = calculate_metrics(solution, controller)
        lyapunov_result = grid_check(controller)

        lyapunov_max_vdot = get_metric(
            lyapunov_result,
            [
                "max_vdot",
                "max_derivative",
                "maximum_vdot",
                "maximum_derivative",
                "max_lyapunov_derivative",
                "max_dvdt",
            ],
        )

        lyapunov_violation_fraction = get_metric(
            lyapunov_result,
            [
                "violation_fraction",
                "violation_ratio",
                "fraction_violations",
                "unstable_fraction",
            ],
        )

        row = {
            "stability_weight": float(stability_weight),
            "epochs": float(epochs),
            "final_total_loss": float(history["total"][-1]),
            "final_imitation_loss": float(history["imitation"][-1]),
            "final_stability_loss": float(history["stability"][-1]),
            "lyapunov_max_vdot": lyapunov_max_vdot,
            "lyapunov_violation_fraction": lyapunov_violation_fraction,
            **metrics,
        }

        rows.append(row)

    return rows


def save_ablation_results_csv(
    rows: list[dict[str, float]],
    output_path: Path,
) -> None:
    """Save stability-weight ablation results as CSV."""

    fieldnames = [
        "stability_weight",
        "epochs",
        "final_total_loss",
        "final_imitation_loss",
        "final_stability_loss",
        "lyapunov_max_vdot",
        "lyapunov_violation_fraction",
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
