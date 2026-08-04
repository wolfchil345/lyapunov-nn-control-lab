from types import SimpleNamespace

import numpy as np
import pytest
import torch

from src.controllers import (
    ZeroAtOriginController,
    calculate_lyapunov_penalty,
    make_dataset,
    train_controller,
)
from src.metrics import calculate_metrics
from src.noise import simulate_with_measurement_noise
from src.parameter_variation import simulate_parameter_variation
from src.region_of_attraction import evaluate_region_of_attraction
from src.reproducibility import set_global_seed
from src.simulation import simulate
from src.system import lqr_controller


@pytest.mark.parametrize("n_samples", [0, -1, True])
def test_dataset_rejects_invalid_sample_count(n_samples):
    with pytest.raises(ValueError, match="n_samples"):
        make_dataset(n_samples)


@pytest.mark.parametrize("duration", [0.0, -1.0, float("nan")])
def test_simulation_rejects_invalid_duration(duration):
    with pytest.raises(ValueError, match="duration"):
        simulate(lqr_controller, np.array([1.0, 0.0]), duration=duration)


@pytest.mark.parametrize(
    "state",
    [np.array([1.0]), np.array([1.0, 0.0, 2.0]), np.array([np.nan, 0.0])],
)
def test_simulation_rejects_invalid_state(state):
    with pytest.raises(ValueError, match="x0"):
        simulate(lqr_controller, state)


def test_noise_simulation_ends_at_requested_nondivisible_duration():
    solution = simulate_with_measurement_noise(
        lqr_controller,
        np.array([1.0, 0.0]),
        noise_std=0.0,
        duration=0.025,
        dt=0.01,
    )

    assert solution.success
    assert solution.t[-1] == pytest.approx(0.025)
    assert np.all(np.diff(solution.t) > 0.0)


def test_parameter_simulation_rejects_nonfinite_parameter():
    with pytest.raises(ValueError, match="mass"):
        simulate_parameter_variation(
            lqr_controller,
            np.array([1.0, 0.0]),
            mass=float("nan"),
            damping=0.4,
            stiffness=2.0,
        )


def test_region_of_attraction_rejects_reversed_range():
    with pytest.raises(ValueError, match="position_range"):
        evaluate_region_of_attraction(
            lqr_controller,
            position_range=(1.0, -1.0),
            num_points=3,
        )


def test_metrics_reject_nonmonotonic_time_vector():
    solution = SimpleNamespace(
        success=True,
        t=np.array([0.0, 1.0, 0.5]),
        y=np.zeros((2, 3)),
    )

    with pytest.raises(ValueError, match="strictly increasing"):
        calculate_metrics(solution, lqr_controller)


def test_lyapunov_penalty_rejects_incompatible_shapes():
    with pytest.raises(ValueError, match="controls"):
        calculate_lyapunov_penalty(
            torch.zeros((2, 2)),
            torch.zeros((2,)),
        )


def test_training_rejects_zero_epochs():
    with pytest.raises(ValueError, match="epochs"):
        train_controller(ZeroAtOriginController(), epochs=0)


def test_global_seed_repeats_numpy_and_torch_sequences():
    set_global_seed(123)
    first_numpy = np.random.random(3)
    first_torch = torch.rand(3)

    set_global_seed(123)

    assert np.array_equal(np.random.random(3), first_numpy)
    assert torch.equal(torch.rand(3), first_torch)
