"""Paired measurement-noise robustness experiments."""

from __future__ import annotations

from collections.abc import Callable, Sequence
import csv
from numbers import Integral
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import numpy as np

from .experimental_seeds import (
    ExperimentSeedPlan,
    aggregate_paired_trials,
    validate_experiment_seed,
)
from .metrics import calculate_metrics_from_control_samples
from .system import A, B
from ._validation import (
    build_time_grid,
    evaluate_controller,
    require_nonempty,
    validate_controller,
    validate_nonnegative_scalar,
    validate_state,
)


NOISE_PAIRING_STRATEGY = (
    "common random-number realizations across noise amplitudes"
)
NOISE_AGGREGATE_METRICS = (
    "final_state_norm",
    "settling_time",
    "quadratic_cost",
    "integrated_squared_control_effort",
    "max_abs_control",
)


def generate_standardized_measurement_noise(
    seed: int,
    num_samples: int,
) -> np.ndarray:
    """Return the exact standardized two-coordinate noise sequence for a seed."""

    seed = validate_experiment_seed(seed)
    if isinstance(num_samples, bool) or not isinstance(num_samples, Integral):
        raise TypeError("num_samples must be a positive integer.")
    if num_samples <= 0:
        raise ValueError("num_samples must be a positive integer.")
    rng = np.random.default_rng(seed)
    return rng.standard_normal((int(num_samples), 2))


def scale_standardized_measurement_noise(
    standardized_noise: np.ndarray,
    noise_std: float,
) -> np.ndarray:
    """Scale one common random-number realization to a noise amplitude."""

    noise_std = validate_nonnegative_scalar(
        noise_std,
        name="noise standard deviation",
    )
    standardized_noise = np.asarray(standardized_noise, dtype=float)
    if standardized_noise.ndim != 2 or standardized_noise.shape[1] != 2:
        raise ValueError("standardized_noise must have shape (num_samples, 2).")
    if not np.all(np.isfinite(standardized_noise)):
        raise ValueError("standardized_noise must contain only finite values.")
    if noise_std == 0.0:
        return np.zeros_like(standardized_noise)
    return noise_std * standardized_noise


def add_measurement_noise(
    state: np.ndarray,
    noise_std: float,
    rng: np.random.Generator,
) -> np.ndarray:
    """Add independent Gaussian noise to both normalized state coordinates."""

    state = validate_state(state, name="state")
    noise_std = validate_nonnegative_scalar(
        noise_std,
        name="noise standard deviation",
    )
    if not isinstance(rng, np.random.Generator):
        raise TypeError("rng must be a numpy.random.Generator.")

    standardized_noise = rng.standard_normal(state.shape)
    if noise_std == 0.0:
        return state.copy()
    return state + noise_std * standardized_noise


def make_noisy_measurement_controller(
    controller: Callable[[np.ndarray], float],
    noise_std: float,
    seed: int = 7,
) -> Callable[[np.ndarray], float]:
    """Wrap a controller with normalized-coordinate measurement noise."""

    controller = validate_controller(controller)
    noise_std = validate_nonnegative_scalar(
        noise_std,
        name="noise standard deviation",
    )
    seed = validate_experiment_seed(seed)
    rng = np.random.default_rng(seed)

    def noisy_controller(true_state: np.ndarray) -> float:
        measured_state = add_measurement_noise(
            true_state,
            noise_std,
            rng,
        )
        return evaluate_controller(controller, measured_state)

    return noisy_controller


def simulate_with_measurement_noise(
    controller: Callable[[np.ndarray], float],
    initial_state: np.ndarray,
    noise_std: float,
    seed: int = 7,
    duration: float = 10.0,
    dt: float = 0.01,
):
    """Simulate using a seed-labelled standardized noise realization.

    Calling this function with the same seed and different ``noise_std`` values
    reuses the same standardized sequence and only changes its amplitude.
    """

    controller = validate_controller(controller)
    initial_state = validate_state(initial_state, name="initial state")
    noise_std = validate_nonnegative_scalar(
        noise_std,
        name="noise standard deviation",
    )
    seed = validate_experiment_seed(seed)

    time = build_time_grid(duration, dt)
    standardized_noise = generate_standardized_measurement_noise(
        seed,
        len(time),
    )
    measurement_noise = scale_standardized_measurement_noise(
        standardized_noise,
        noise_std,
    )
    states = np.zeros((2, len(time)), dtype=float)
    controls = np.zeros(len(time), dtype=float)
    states[:, 0] = initial_state

    for index in range(len(time)):
        true_state = states[:, index]
        measured_state = true_state + measurement_noise[index]
        controls[index] = evaluate_controller(controller, measured_state)

        if index == len(time) - 1:
            break

        state_dot = A @ true_state + B[:, 0] * controls[index]
        step = time[index + 1] - time[index]
        states[:, index + 1] = true_state + step * state_dot

        if not np.all(np.isfinite(states[:, index + 1])):
            return SimpleNamespace(
                t=time[: index + 2],
                y=states[:, : index + 2],
                controls=controls[: index + 2],
                standardized_measurement_noise=standardized_noise[: index + 2],
                measurement_noise=measurement_noise[: index + 2],
                seed=seed,
                noise_std=noise_std,
                success=False,
                message="Non-finite state encountered.",
            )

    return SimpleNamespace(
        t=time,
        y=states,
        controls=controls,
        standardized_measurement_noise=standardized_noise,
        measurement_noise=measurement_noise,
        seed=seed,
        noise_std=noise_std,
        success=True,
        message="Simulation completed successfully.",
    )


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


def run_measurement_noise_trials(
    controller: Callable[[np.ndarray], float],
    initial_state: np.ndarray,
    noise_stds: Sequence[float],
    *,
    seed_plan: ExperimentSeedPlan | None = None,
    base_seed: int = 7,
    num_repeats: int = 1,
    duration: float = 10.0,
    dt: float = 0.01,
) -> tuple[
    list[dict[str, float | int | str]],
    dict[tuple[float, int], Any],
]:
    """Evaluate every noise amplitude with every matched seed."""

    controller = validate_controller(controller)
    initial_state = validate_state(initial_state, name="initial state")
    require_nonempty(noise_stds, name="noise_stds")
    levels = tuple(
        validate_nonnegative_scalar(level, name="noise standard deviation")
        for level in noise_stds
    )
    if len(set(levels)) != len(levels):
        raise ValueError("noise_stds must not contain duplicates.")

    plan = _resolve_seed_plan(
        seed_plan,
        base_seed=base_seed,
        num_repeats=num_repeats,
    )
    provenance = plan.metadata(pairing_strategy=NOISE_PAIRING_STRATEGY)
    rows: list[dict[str, float | int | str]] = []
    solutions: dict[tuple[float, int], Any] = {}

    for noise_std in levels:
        for seed in plan.seeds:
            solution = simulate_with_measurement_noise(
                controller,
                initial_state,
                noise_std=noise_std,
                seed=seed,
                duration=duration,
                dt=dt,
            )
            if not solution.success:
                raise RuntimeError(
                    "Measurement-noise simulation failed for "
                    f"noise_std={noise_std}, seed={seed}: {solution.message}"
                )

            metrics = calculate_metrics_from_control_samples(
                solution,
                solution.controls,
            )
            rows.append(
                {
                    "noise_std": noise_std,
                    "seed": seed,
                    **provenance,
                    **metrics,
                }
            )
            solutions[(noise_std, seed)] = solution

    return rows, solutions


def aggregate_noise_results(
    rows: Sequence[dict[str, Any]],
) -> list[dict[str, float | int | str]]:
    """Aggregate paired noise trials by normalized noise amplitude."""

    return aggregate_paired_trials(
        rows,
        condition_key="noise_std",
        metric_names=NOISE_AGGREGATE_METRICS,
    )


def _write_csv(
    rows: Sequence[dict[str, Any]],
    output_path: Path,
    fieldnames: Sequence[str],
) -> None:
    require_nonempty(rows, name="noise rows")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def save_noise_trial_results_csv(
    rows: Sequence[dict[str, Any]],
    output_path: Path,
) -> None:
    """Save one row per ``noise_std x seed`` trial."""

    _write_csv(
        rows,
        output_path,
        [
            "noise_std",
            "seed",
            "base_seed",
            "seed_list",
            "repeat_count",
            "pairing_strategy",
            "final_state_norm",
            "settling_time",
            "settling_time_s",
            "quadratic_cost",
            "integrated_squared_control_effort",
            "control_energy",
            "max_abs_control",
        ],
    )


def save_noise_aggregate_csv(
    rows: Sequence[dict[str, Any]],
    output_path: Path,
) -> None:
    """Save one aggregate row per normalized noise amplitude."""

    fields = [
        "noise_std",
        "n",
        "base_seed",
        "seed_list",
        "repeat_count",
        "pairing_strategy",
    ]
    for metric_name in NOISE_AGGREGATE_METRICS:
        fields.extend(
            [
                f"{metric_name}_mean",
                f"{metric_name}_sample_std",
                f"{metric_name}_standard_error",
            ]
        )
    _write_csv(rows, output_path, fields)
