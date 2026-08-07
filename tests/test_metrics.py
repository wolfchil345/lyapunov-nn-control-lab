import math
from types import SimpleNamespace

import numpy as np
import pytest

from lyapunov_nn_control_lab.metrics import (
    calculate_metrics,
    calculate_metrics_from_control_samples,
)
from lyapunov_nn_control_lab.simulation import simulate
from lyapunov_nn_control_lab.system import lqr_controller


def test_lqr_performance_metrics_are_valid():
    initial_state = np.array(
        [1.5, 0.0],
        dtype=float,
    )

    solution = simulate(
        lqr_controller,
        initial_state,
    )

    metrics = calculate_metrics(
        solution,
        lqr_controller,
    )

    assert solution.success
    assert metrics["final_state_norm"] < 1e-3
    assert math.isfinite(metrics["settling_time_s"])
    assert metrics["settling_time_s"] > 0.0
    assert metrics["quadratic_cost"] > 0.0
    assert metrics["settling_time"] == metrics["settling_time_s"]
    assert metrics["integrated_squared_control_effort"] > 0.0
    assert metrics["integrated_squared_control_effort"] == metrics[
        "control_energy"
    ]
    assert metrics["control_energy"] > 0.0
    assert metrics["max_abs_control"] > 0.0


def test_metrics_reject_empty_solution_data():
    solution = SimpleNamespace(
        success=True,
        t=np.array([]),
        y=np.empty((2, 0)),
    )

    with pytest.raises(ValueError, match="nonempty"):
        calculate_metrics(solution, lqr_controller)


def test_metrics_accept_recorded_stochastic_control_samples():
    solution = SimpleNamespace(
        success=True,
        t=np.array([0.0, 0.5, 1.0]),
        y=np.array([[1.0, 0.5, 0.0], [0.0, 0.0, 0.0]]),
    )

    metrics = calculate_metrics_from_control_samples(
        solution,
        np.array([-1.0, -0.5, 0.0]),
    )

    assert metrics["final_state_norm"] == 0.0
    assert metrics["quadratic_cost"] > 0.0
    assert metrics["integrated_squared_control_effort"] == pytest.approx(0.375)
    assert metrics["max_abs_control"] == 1.0


def test_recorded_control_metrics_require_one_control_per_sample():
    solution = SimpleNamespace(
        success=True,
        t=np.array([0.0, 1.0]),
        y=np.zeros((2, 2)),
    )

    with pytest.raises(ValueError, match="one value per solution sample"):
        calculate_metrics_from_control_samples(solution, np.array([0.0]))
