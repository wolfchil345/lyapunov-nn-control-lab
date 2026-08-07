import csv
import random
from pathlib import Path

import numpy as np
import torch

from .controllers import (
    ZeroAtOriginController,
    make_nn_controller,
    train_controller,
)
from .lyapunov import DEFAULT_DECAY_MARGIN, grid_check
from .metrics import calculate_metrics
from .simulation import simulate
from ._validation import require_nonempty, validate_seed, validate_state


def set_ablation_seed(seed: int) -> None:
    """Set random seeds for repeatable ablation runs."""

    seed = validate_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.set_num_threads(1)


def run_stability_weight_ablation(
    stability_weights: list[float],
    initial_state: np.ndarray,
    epochs: int = 300,
    stability_margin: float = DEFAULT_DECAY_MARGIN,
    base_seed: int = 700,
) -> list[dict[str, float]]:
    """Train controllers with different Lyapunov penalty weights."""

    require_nonempty(stability_weights, name="stability_weights")
    initial_state = validate_state(initial_state, name="initial_state")
    base_seed = validate_seed(base_seed)
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
        lyapunov_result = grid_check(
            controller,
            decay_margin=stability_margin,
        )

        row = {
            "stability_weight": float(stability_weight),
            "decay_margin": float(stability_margin),
            "epochs": float(epochs),
            "final_total_loss": float(history["total"][-1]),
            "final_imitation_loss": float(history["imitation"][-1]),
            "final_stability_loss": float(history["stability"][-1]),
            "max_vdot": float(lyapunov_result["max_vdot"]),
            "max_decay_residual": float(
                lyapunov_result["max_decay_residual"]
            ),
            "derivative_violation_fraction": float(
                lyapunov_result["derivative_violation_fraction"]
            ),
            "decay_margin_violation_fraction": float(
                lyapunov_result["decay_margin_violation_fraction"]
            ),
            **metrics,
        }

        rows.append(row)

    return rows


def save_ablation_results_csv(
    rows: list[dict[str, float]],
    output_path: Path,
) -> None:
    """Save stability-weight ablation results as CSV."""

    require_nonempty(rows, name="ablation rows")
    fieldnames = [
        "stability_weight",
        "decay_margin",
        "epochs",
        "final_total_loss",
        "final_imitation_loss",
        "final_stability_loss",
        "max_vdot",
        "max_decay_residual",
        "derivative_violation_fraction",
        "decay_margin_violation_fraction",
        "final_state_norm",
        "settling_time",
        "settling_time_s",
        "quadratic_cost",
        "integrated_squared_control_effort",
        "control_energy",
        "max_abs_control",
    ]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
