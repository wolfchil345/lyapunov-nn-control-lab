import math
from types import SimpleNamespace

import numpy as np
import pytest

from lyapunov_nn_control_lab.metrics import calculate_metrics
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
