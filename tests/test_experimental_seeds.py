import math
import random

import numpy as np
import pytest
import torch

from lyapunov_nn_control_lab.controllers import (
    ZeroAtOriginController,
    train_controller,
)
from lyapunov_nn_control_lab.experimental_seeds import (
    ExperimentSeedPlan,
    MAX_EXPERIMENT_SEED,
    aggregate_paired_trials,
    seed_random_generators,
    validate_paired_seed_sets,
)


def test_consecutive_seed_plan_is_explicit_and_transparent():
    plan = ExperimentSeedPlan.consecutive(base_seed=40, num_repeats=3)

    assert plan.base_seed == 40
    assert plan.seeds == (40, 41, 42)
    assert plan.repeat_count == 3
    assert plan.metadata(pairing_strategy="paired test") == {
        "base_seed": 40,
        "seed_list": "40;41;42",
        "repeat_count": 3,
        "pairing_strategy": "paired test",
    }


@pytest.mark.parametrize(
    ("factory", "match"),
    [
        (lambda: ExperimentSeedPlan.explicit([]), "must not be empty"),
        (lambda: ExperimentSeedPlan.explicit([7, 7]), "duplicates"),
        (
            lambda: ExperimentSeedPlan.explicit([MAX_EXPERIMENT_SEED + 1]),
            "no greater than",
        ),
        (
            lambda: ExperimentSeedPlan.consecutive(7, 0),
            "positive integer",
        ),
    ],
)
def test_seed_plan_rejects_invalid_designs(factory, match):
    with pytest.raises(ValueError, match=match):
        factory()


def test_seed_plan_rejects_noninteger_repeat_count():
    with pytest.raises(TypeError, match="positive integer"):
        ExperimentSeedPlan.consecutive(7, 1.5)


def test_central_seeding_reproduces_cpu_rngs():
    seed_random_generators(23)
    first = (random.random(), np.random.random(), torch.rand(3))

    seed_random_generators(23)
    second = (random.random(), np.random.random(), torch.rand(3))

    assert first[0] == second[0]
    assert first[1] == second[1]
    assert torch.equal(first[2], second[2])


def test_central_seeding_includes_cuda_when_available(monkeypatch):
    calls = []
    monkeypatch.setattr(torch.cuda, "is_available", lambda: True)
    monkeypatch.setattr(torch.cuda, "manual_seed_all", calls.append)

    seed_random_generators(37)

    assert 37 in calls


def test_repeated_cpu_training_reproduces_repository_quantities():
    histories = []
    parameters = []
    for _repeat in range(2):
        seed_random_generators(29)
        model = ZeroAtOriginController()
        histories.append(
            train_controller(model, epochs=2, stability_weight=10.0)
        )
        parameters.append(
            torch.cat(
                [parameter.detach().flatten() for parameter in model.parameters()]
            ).clone()
        )

    assert histories[0] == histories[1]
    assert torch.equal(parameters[0], parameters[1])


def test_paired_seed_validation_detects_mismatched_conditions():
    rows = [
        {"condition": 0.0, "seed": 7},
        {"condition": 0.0, "seed": 8},
        {"condition": 1.0, "seed": 7},
    ]

    with pytest.raises(ValueError, match="same seed set"):
        validate_paired_seed_sets(rows, condition_key="condition")


def test_single_repeat_aggregate_marks_variability_unavailable():
    rows = [
        {
            "condition": 0.0,
            "seed": 7,
            "metric": 2.0,
            "base_seed": 7,
            "pairing_strategy": "paired test",
        },
    ]

    aggregate = aggregate_paired_trials(
        rows,
        condition_key="condition",
        metric_names=["metric"],
    )[0]

    assert aggregate["n"] == 1
    assert aggregate["metric_mean"] == 2.0
    assert math.isnan(aggregate["metric_sample_std"])
    assert math.isnan(aggregate["metric_standard_error"])


def test_multiple_repeat_aggregate_uses_sample_statistics():
    rows = [
        {"condition": condition, "seed": seed, "metric": value}
        for condition, values in [(0.0, [1.0, 3.0]), (1.0, [2.0, 4.0])]
        for seed, value in zip([7, 8], values, strict=True)
    ]

    aggregates = aggregate_paired_trials(
        rows,
        condition_key="condition",
        metric_names=["metric"],
    )

    assert [row["n"] for row in aggregates] == [2, 2]
    assert aggregates[0]["metric_mean"] == 2.0
    assert aggregates[0]["metric_sample_std"] == pytest.approx(np.sqrt(2.0))
    assert aggregates[0]["metric_standard_error"] == pytest.approx(1.0)
