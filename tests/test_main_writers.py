from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


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


def test_save_metrics_csv_rejects_empty_rows(tmp_path):
    with pytest.raises(ValueError, match="must not be empty"):
        project_main.save_metrics_csv([], tmp_path / "metrics.csv")
