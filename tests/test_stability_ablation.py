from pathlib import Path

import numpy as np
import pytest

from lyapunov_nn_control_lab.plotting import save_stability_weight_ablation_plot
from lyapunov_nn_control_lab.stability_ablation import (
    run_stability_weight_ablation,
    save_ablation_results_csv,
)


def sample_rows():
    return [
        {
            "stability_weight": 0.0,
            "epochs": 10.0,
            "final_total_loss": 1.0,
            "final_imitation_loss": 1.0,
            "final_stability_loss": 0.5,
            "lyapunov_max_vdot": 0.2,
            "lyapunov_violation_fraction": 0.4,
            "final_state_norm": 0.1,
            "settling_time_s": 3.0,
            "quadratic_cost": 5.0,
            "control_energy": 2.0,
            "max_abs_control": 1.0,
        },
        {
            "stability_weight": 10.0,
            "epochs": 10.0,
            "final_total_loss": 0.5,
            "final_imitation_loss": 0.4,
            "final_stability_loss": 0.1,
            "lyapunov_max_vdot": -0.1,
            "lyapunov_violation_fraction": 0.05,
            "final_state_norm": 0.01,
            "settling_time_s": 2.0,
            "quadratic_cost": 4.0,
            "control_energy": 1.5,
            "max_abs_control": 0.8,
        },
    ]


def test_save_ablation_results_csv_creates_file(tmp_path):
    output_path = tmp_path / "nested" / "ablation.csv"

    save_ablation_results_csv(
        sample_rows(),
        output_path,
    )

    assert output_path.exists()
    assert "stability_weight" in output_path.read_text()


def test_save_stability_weight_ablation_plot_creates_file(tmp_path):
    save_stability_weight_ablation_plot(
        sample_rows(),
        tmp_path,
    )

    assert (tmp_path / "stability_weight_ablation.png").exists()


def test_ablation_writers_reject_empty_required_rows(tmp_path):
    with pytest.raises(ValueError, match="must not be empty"):
        save_ablation_results_csv([], tmp_path / "ablation.csv")
    with pytest.raises(ValueError, match="must not be empty"):
        save_stability_weight_ablation_plot([], tmp_path)


def test_ablation_runner_rejects_empty_weights():
    with pytest.raises(ValueError, match="must not be empty"):
        run_stability_weight_ablation([], np.array([1.0, 0.0]))
