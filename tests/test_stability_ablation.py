from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

import lyapunov_nn_control_lab.stability_ablation as stability_ablation
from lyapunov_nn_control_lab.plotting import save_stability_weight_ablation_plot
from lyapunov_nn_control_lab.stability_ablation import (
    run_stability_weight_ablation,
    save_ablation_results_csv,
)


def sample_rows():
    return [
        {
            "stability_weight": 0.0,
            "decay_margin": 0.05,
            "epochs": 10.0,
            "final_total_loss": 1.0,
            "final_imitation_loss": 1.0,
            "final_stability_loss": 0.5,
            "max_vdot": 0.2,
            "max_decay_residual": 0.3,
            "derivative_violation_fraction": 0.4,
            "decay_margin_violation_fraction": 0.5,
            "final_state_norm": 0.1,
            "settling_time": 3.0,
            "settling_time_s": 3.0,
            "quadratic_cost": 5.0,
            "integrated_squared_control_effort": 2.0,
            "control_energy": 2.0,
            "max_abs_control": 1.0,
        },
        {
            "stability_weight": 10.0,
            "decay_margin": 0.05,
            "epochs": 10.0,
            "final_total_loss": 0.5,
            "final_imitation_loss": 0.4,
            "final_stability_loss": 0.1,
            "max_vdot": -0.1,
            "max_decay_residual": -0.05,
            "derivative_violation_fraction": 0.0,
            "decay_margin_violation_fraction": 0.05,
            "final_state_norm": 0.01,
            "settling_time": 2.0,
            "settling_time_s": 2.0,
            "quadratic_cost": 4.0,
            "integrated_squared_control_effort": 1.5,
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
    csv_text = output_path.read_text()
    assert "stability_weight" in csv_text
    assert "derivative_violation_fraction" in csv_text
    assert "decay_margin_violation_fraction" in csv_text
    assert "lyapunov_violation_fraction" not in csv_text


def test_save_stability_weight_ablation_plot_creates_file(tmp_path):
    save_stability_weight_ablation_plot(
        sample_rows(),
        tmp_path,
    )

    assert (tmp_path / "stability_weight_ablation.png").exists()


def test_ablation_plot_accepts_precise_control_effort_name_without_alias(
    tmp_path,
):
    rows = sample_rows()
    for row in rows:
        row.pop("control_energy")

    save_stability_weight_ablation_plot(rows, tmp_path)

    assert (tmp_path / "stability_weight_ablation.png").exists()


def test_ablation_writers_reject_empty_required_rows(tmp_path):
    with pytest.raises(ValueError, match="must not be empty"):
        save_ablation_results_csv([], tmp_path / "ablation.csv")
    with pytest.raises(ValueError, match="must not be empty"):
        save_stability_weight_ablation_plot([], tmp_path)


def test_ablation_runner_rejects_empty_weights():
    with pytest.raises(ValueError, match="must not be empty"):
        run_stability_weight_ablation([], np.array([1.0, 0.0]))


def test_ablation_reports_both_lyapunov_conditions(monkeypatch):
    captured = {}
    monkeypatch.setattr(stability_ablation, "ZeroAtOriginController", object)
    monkeypatch.setattr(
        stability_ablation,
        "train_controller",
        lambda *_args, **_kwargs: {
            "total": [1.0],
            "imitation": [0.9],
            "stability": [0.1],
        },
    )
    monkeypatch.setattr(
        stability_ablation,
        "make_nn_controller",
        lambda _model: (lambda _state: 0.0),
    )
    monkeypatch.setattr(
        stability_ablation,
        "simulate",
        lambda *_args, **_kwargs: SimpleNamespace(success=True),
    )
    monkeypatch.setattr(
        stability_ablation,
        "calculate_metrics",
        lambda *_args, **_kwargs: {
            "final_state_norm": 0.1,
            "settling_time": 1.0,
            "settling_time_s": 1.0,
            "quadratic_cost": 2.0,
            "integrated_squared_control_effort": 3.0,
            "control_energy": 3.0,
            "max_abs_control": 4.0,
        },
    )

    def fake_grid_check(_controller, *, decay_margin):
        captured["decay_margin"] = decay_margin
        return {
            "max_vdot": -0.01,
            "max_decay_residual": 0.02,
            "derivative_violation_fraction": 0.0,
            "decay_margin_violation_fraction": 0.25,
        }

    monkeypatch.setattr(stability_ablation, "grid_check", fake_grid_check)

    row = run_stability_weight_ablation(
        [10.0],
        np.array([1.0, 0.0]),
        epochs=1,
        stability_margin=0.05,
    )[0]

    assert captured["decay_margin"] == 0.05
    assert row["decay_margin"] == 0.05
    assert row["derivative_violation_fraction"] == 0.0
    assert row["decay_margin_violation_fraction"] == 0.25
    assert row["max_vdot"] == -0.01
    assert row["max_decay_residual"] == 0.02
