from dataclasses import replace

import numpy as np
import pytest

from lyapunov_nn_control_lab.finite_horizon_convergence import (
    FiniteHorizonConvergenceResult,
)
from lyapunov_nn_control_lab.plotting import (
    save_finite_horizon_convergence_comparison_plot,
    save_finite_horizon_convergence_plot,
)


def make_result(label: str) -> FiniteHorizonConvergenceResult:
    positions = np.linspace(-1.0, 1.0, 3)
    velocities = np.linspace(-1.0, 1.0, 3)
    convergence_map = np.array(
        [
            [False, True, False],
            [True, True, True],
            [False, True, False],
        ]
    )
    final_norm_map = np.array(
        [
            [0.5, 0.1, 0.5],
            [0.1, 0.0, 0.1],
            [0.5, 0.1, 0.5],
        ]
    )
    return FiniteHorizonConvergenceResult(
        positions=positions,
        velocities=velocities,
        convergence_map=convergence_map,
        final_norm_map=final_norm_map,
        horizon=8.0,
        convergence_tolerance=0.1,
        position_bounds=(-1.0, 1.0),
        velocity_bounds=(-1.0, 1.0),
        grid_resolution=3,
        tested_count=9,
        converged_count=5,
        convergence_fraction=5 / 9,
        controller_label=label,
    )


def test_finite_horizon_plot_uses_future_filename(tmp_path):
    save_finite_horizon_convergence_plot(make_result("LQR"), tmp_path)

    assert (tmp_path / "finite_horizon_convergence.png").exists()
    assert not (tmp_path / "region_of_attraction.png").exists()


def test_comparison_plot_uses_future_filename(tmp_path):
    comparison = {
        "LQR": make_result("LQR"),
        "Neural network": make_result("Neural network"),
    }

    save_finite_horizon_convergence_comparison_plot(comparison, tmp_path)

    assert (
        tmp_path / "finite_horizon_convergence_comparison.png"
    ).exists()
    assert not (tmp_path / "region_of_attraction_comparison.png").exists()


def test_comparison_rejects_empty_or_incompatible_results(tmp_path):
    with pytest.raises(ValueError, match="must not be empty"):
        save_finite_horizon_convergence_comparison_plot({}, tmp_path)

    incompatible = replace(make_result("Neural network"), horizon=4.0)

    with pytest.raises(ValueError, match="same horizon"):
        save_finite_horizon_convergence_comparison_plot(
            {"LQR": make_result("LQR"), "NN": incompatible},
            tmp_path,
        )
