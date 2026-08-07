from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
MAIN_PATH = ROOT / "main.py"

spec = importlib.util.spec_from_file_location("project_main", MAIN_PATH)
project_main = importlib.util.module_from_spec(spec)
assert spec is not None
assert spec.loader is not None
spec.loader.exec_module(project_main)


def test_save_metrics_csv_creates_parent_directory(tmp_path):
    output_path = tmp_path / "nested" / "metrics.csv"
    rows = [
        {
            "initial_position": 1.0,
            "initial_velocity": 0.0,
            "controller": "LQR",
            "control_limit": "none",
            "final_state_norm": 0.01,
            "settling_time_s": 2.0,
            "quadratic_cost": 4.0,
            "control_energy": 1.0,
            "max_abs_control": 2.0,
        }
    ]

    project_main.save_metrics_csv(rows, output_path)

    assert output_path.exists()
    header = output_path.read_text(encoding="utf-8").splitlines()[0]
    assert "settling_time" in header
    assert "integrated_squared_control_effort" in header


def test_save_metrics_csv_rejects_empty_rows(tmp_path):
    with pytest.raises(ValueError, match="must not be empty"):
        project_main.save_metrics_csv([], tmp_path / "metrics.csv")


def test_scientific_configuration_snapshot_matches_effective_defaults():
    config = project_main.scientific_configuration_snapshot()
    np.testing.assert_array_equal(
        config["plant"]["A"],
        [[0.0, 1.0], [-2.0, -0.4]],
    )
    assert config["training"] == {
        "seed": 7,
        "epochs": 1000,
        "stability_weight": 10.0,
        "decay_margin": 0.05,
    }
    assert config["stability_weight_ablation"]["seeds"] == [700, 701, 702]
    assert config["measurement_noise"]["seeds"] == [7, 8, 9]
    assert config["finite_horizon_convergence"]["horizon"] == 8.0
    assert config["lyapunov_evaluation"]["numerical_tolerance"] == 1e-9
