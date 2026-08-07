"""Explicit seed plans for paired, repeatable experiments.

Fixed seeds make CPU experiments repeatable under the same software and
hardware conditions.  They do not guarantee fully deterministic execution on
every accelerator or across dependency versions.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
import random
from typing import Any

import numpy as np
import torch

from ._validation import validate_seed


MAX_EXPERIMENT_SEED = 2**32 - 1


def validate_experiment_seed(seed: Any) -> int:
    """Return a seed supported by Python, NumPy, and PyTorch seeding APIs."""

    result = validate_seed(seed)
    if result > MAX_EXPERIMENT_SEED:
        raise ValueError(
            f"seed must be no greater than {MAX_EXPERIMENT_SEED}."
        )
    return result


@dataclass(frozen=True, slots=True)
class ExperimentSeedPlan:
    """The exact random seeds used as paired experimental repeats."""

    seeds: tuple[int, ...]
    base_seed: int | None = None

    def __post_init__(self) -> None:
        seeds = tuple(validate_experiment_seed(seed) for seed in self.seeds)
        if not seeds:
            raise ValueError("seeds must not be empty.")
        if len(set(seeds)) != len(seeds):
            raise ValueError("seeds must not contain duplicates.")

        base_seed = self.base_seed
        if base_seed is not None:
            base_seed = validate_experiment_seed(base_seed)

        object.__setattr__(self, "seeds", seeds)
        object.__setattr__(self, "base_seed", base_seed)

    @classmethod
    def consecutive(
        cls,
        base_seed: int,
        num_repeats: int,
    ) -> "ExperimentSeedPlan":
        """Build a transparent consecutive seed sequence."""

        base_seed = validate_experiment_seed(base_seed)
        if isinstance(num_repeats, bool) or not isinstance(num_repeats, int):
            raise TypeError("num_repeats must be a positive integer.")
        if num_repeats <= 0:
            raise ValueError("num_repeats must be a positive integer.")
        final_seed = base_seed + num_repeats - 1
        if final_seed > MAX_EXPERIMENT_SEED:
            raise ValueError(
                "base_seed + num_repeats - 1 exceeds the supported seed range."
            )
        return cls(
            seeds=tuple(range(base_seed, final_seed + 1)),
            base_seed=base_seed,
        )

    @classmethod
    def explicit(cls, seeds: Sequence[int]) -> "ExperimentSeedPlan":
        """Build a plan from an explicitly supplied seed sequence."""

        return cls(seeds=tuple(seeds), base_seed=None)

    @property
    def repeat_count(self) -> int:
        """Return the number of paired repeats."""

        return len(self.seeds)

    def metadata(self, *, pairing_strategy: str) -> dict[str, int | str]:
        """Return CSV/report-friendly methodological provenance."""

        if not pairing_strategy.strip():
            raise ValueError("pairing_strategy must not be empty.")
        return {
            "base_seed": "" if self.base_seed is None else self.base_seed,
            "seed_list": ";".join(str(seed) for seed in self.seeds),
            "repeat_count": self.repeat_count,
            "pairing_strategy": pairing_strategy,
        }


def seed_random_generators(seed: int) -> int:
    """Seed the Python, NumPy, and PyTorch RNGs used by this project.

    CUDA generators are seeded when CUDA is available.  This does not enable
    PyTorch's deterministic-algorithm mode and therefore is not a universal
    guarantee of bitwise deterministic CUDA execution.
    """

    seed = validate_experiment_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    return seed


def validate_paired_seed_sets(
    rows: Sequence[Mapping[str, Any]],
    *,
    condition_key: str,
) -> tuple[int, ...]:
    """Require every experimental condition to use the same unique seeds."""

    if not rows:
        raise ValueError("trial rows must not be empty.")

    seeds_by_condition: dict[Any, list[int]] = {}
    for row in rows:
        if condition_key not in row or "seed" not in row:
            raise KeyError(
                f"each trial row must contain {condition_key!r} and 'seed'."
            )
        seed = validate_experiment_seed(row["seed"])
        seeds_by_condition.setdefault(row[condition_key], []).append(seed)

    reference: tuple[int, ...] | None = None
    for condition, seeds in seeds_by_condition.items():
        if len(seeds) != len(set(seeds)):
            raise ValueError(
                f"condition {condition!r} contains duplicate seed trials."
            )
        current = tuple(sorted(seeds))
        if reference is None:
            reference = current
        elif current != reference:
            raise ValueError(
                f"all {condition_key} conditions must use the same seed set."
            )

    assert reference is not None
    return reference


def aggregate_paired_trials(
    rows: Sequence[Mapping[str, Any]],
    *,
    condition_key: str,
    metric_names: Sequence[str],
) -> list[dict[str, float | int | str]]:
    """Calculate means, sample deviations, and standard errors by condition."""

    paired_seeds = validate_paired_seed_sets(rows, condition_key=condition_key)
    if not metric_names:
        raise ValueError("metric_names must not be empty.")

    grouped: dict[Any, list[Mapping[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(row[condition_key], []).append(row)

    aggregates: list[dict[str, float | int | str]] = []
    for condition in sorted(grouped):
        group = grouped[condition]
        n = len(group)
        first = group[0]
        aggregate: dict[str, float | int | str] = {
            condition_key: float(condition),
            "n": n,
            "base_seed": first.get("base_seed", ""),
            "seed_list": ";".join(str(seed) for seed in paired_seeds),
            "repeat_count": n,
            "pairing_strategy": str(first.get("pairing_strategy", "")),
        }

        for metric_name in metric_names:
            try:
                values = np.asarray(
                    [float(row[metric_name]) for row in group],
                    dtype=float,
                )
            except KeyError as exc:
                raise KeyError(
                    f"each trial row must contain metric {metric_name!r}."
                ) from exc

            mean = float(np.mean(values))
            if n > 1:
                sample_std = float(np.std(values, ddof=1))
                standard_error = float(sample_std / np.sqrt(n))
            else:
                sample_std = float("nan")
                standard_error = float("nan")

            aggregate[f"{metric_name}_mean"] = mean
            aggregate[f"{metric_name}_sample_std"] = sample_std
            aggregate[f"{metric_name}_standard_error"] = standard_error

        aggregates.append(aggregate)

    return aggregates
