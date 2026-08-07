"""Paired, repeated stability-weight ablation experiments."""

from __future__ import annotations

from collections.abc import Sequence
import csv
from pathlib import Path
from typing import Any

import numpy as np
import torch

from .controllers import (
    ZeroAtOriginController,
    make_nn_controller,
    train_controller,
)
from .experimental_seeds import (
    ExperimentSeedPlan,
    aggregate_paired_trials,
    seed_random_generators,
)
from .lyapunov import DEFAULT_DECAY_MARGIN, grid_check
from .metrics import calculate_metrics
from .simulation import simulate
from ._validation import (
    require_nonempty,
    validate_nonnegative_scalar,
    validate_state,
)


ABLATION_PAIRING_STRATEGY = "paired seeds across all stability weights"
ABLATION_AGGREGATE_METRICS = (
    "final_total_loss",
    "final_imitation_loss",
    "final_stability_loss",
    "max_vdot",
    "max_decay_residual",
    "derivative_violation_fraction",
    "decay_margin_violation_fraction",
    "final_state_norm",
    "settling_time",
    "quadratic_cost",
    "integrated_squared_control_effort",
    "max_abs_control",
)


def set_ablation_seed(seed: int) -> None:
    """Seed all project RNGs before one ablation training trial."""

    seed_random_generators(seed)
    torch.set_num_threads(1)


def _resolve_seed_plan(
    seed_plan: ExperimentSeedPlan | None,
    *,
    base_seed: int,
    num_repeats: int,
) -> ExperimentSeedPlan:
    if seed_plan is not None:
        if not isinstance(seed_plan, ExperimentSeedPlan):
            raise TypeError("seed_plan must be an ExperimentSeedPlan.")
        return seed_plan
    return ExperimentSeedPlan.consecutive(base_seed, num_repeats)


def run_stability_weight_ablation(
    stability_weights: Sequence[float],
    initial_state: np.ndarray,
    epochs: int = 300,
    stability_margin: float = DEFAULT_DECAY_MARGIN,
    base_seed: int = 700,
    num_repeats: int = 1,
    *,
    seed_plan: ExperimentSeedPlan | None = None,
) -> list[dict[str, float | int | str]]:
    """Evaluate every stability weight with the same repeated seed set.

    The returned table contains one raw row for every
    ``stability_weight x seed`` trial.  Random seed is a paired nuisance factor;
    it is never derived from a weight's list index.
    """

    require_nonempty(stability_weights, name="stability_weights")
    weights = tuple(
        validate_nonnegative_scalar(weight, name="stability_weight")
        for weight in stability_weights
    )
    if len(set(weights)) != len(weights):
        raise ValueError("stability_weights must not contain duplicates.")

    initial_state = validate_state(initial_state, name="initial_state")
    plan = _resolve_seed_plan(
        seed_plan,
        base_seed=base_seed,
        num_repeats=num_repeats,
    )
    provenance = plan.metadata(pairing_strategy=ABLATION_PAIRING_STRATEGY)
    rows: list[dict[str, float | int | str]] = []

    for stability_weight in weights:
        for seed in plan.seeds:
            set_ablation_seed(seed)

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
                    "Simulation failed for "
                    f"stability_weight={stability_weight}, seed={seed}."
                )

            metrics = calculate_metrics(solution, controller)
            lyapunov_result = grid_check(
                controller,
                decay_margin=stability_margin,
            )

            row: dict[str, float | int | str] = {
                "stability_weight": stability_weight,
                "seed": seed,
                **provenance,
                "decay_margin": float(stability_margin),
                "epochs": int(epochs),
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


def aggregate_ablation_results(
    rows: Sequence[dict[str, Any]],
) -> list[dict[str, float | int | str]]:
    """Aggregate paired ablation trials by stability weight."""

    return aggregate_paired_trials(
        rows,
        condition_key="stability_weight",
        metric_names=ABLATION_AGGREGATE_METRICS,
    )


_LEGACY_TRIAL_FIELDS = [
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

_PAIRED_TRIAL_FIELDS = [
    "stability_weight",
    "seed",
    "base_seed",
    "seed_list",
    "repeat_count",
    "pairing_strategy",
    *_LEGACY_TRIAL_FIELDS[1:],
]


def _write_csv(
    rows: Sequence[dict[str, Any]],
    output_path: Path,
    fieldnames: Sequence[str],
) -> None:
    require_nonempty(rows, name="ablation rows")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def save_ablation_results_csv(
    rows: Sequence[dict[str, Any]],
    output_path: Path,
) -> None:
    """Save raw ablation trials, retaining the historical schema fallback."""

    require_nonempty(rows, name="ablation rows")
    fieldnames = (
        _PAIRED_TRIAL_FIELDS if "seed" in rows[0] else _LEGACY_TRIAL_FIELDS
    )
    _write_csv(rows, output_path, fieldnames)


def save_ablation_aggregate_csv(
    rows: Sequence[dict[str, Any]],
    output_path: Path,
) -> None:
    """Save one aggregate row per stability weight."""

    fields = [
        "stability_weight",
        "n",
        "base_seed",
        "seed_list",
        "repeat_count",
        "pairing_strategy",
    ]
    for metric_name in ABLATION_AGGREGATE_METRICS:
        fields.extend(
            [
                f"{metric_name}_mean",
                f"{metric_name}_sample_std",
                f"{metric_name}_standard_error",
            ]
        )
    _write_csv(rows, output_path, fields)
