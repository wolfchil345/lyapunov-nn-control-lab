from pathlib import Path

import numpy as np
import pytest

import lyapunov_nn_control_lab.reporting as reporting
from lyapunov_nn_control_lab.finite_horizon_convergence import (
    FiniteHorizonConvergenceResult,
)
from lyapunov_nn_control_lab.reporting import (
    escape_markdown_table_cell,
    format_markdown_table,
    generate_experiment_report,
    read_csv_rows,
)


def test_read_csv_rows_reads_limited_rows(tmp_path):
    csv_path = tmp_path / "data.csv"
    csv_path.write_text(
        "name,value\n"
        "a,1\n"
        "b,2\n",
        encoding="utf-8",
    )

    rows = read_csv_rows(
        csv_path,
        max_rows=1,
    )

    assert len(rows) == 1
    assert rows[0]["name"] == "a"


def test_read_csv_rows_streams_only_requested_rows(tmp_path, monkeypatch):
    csv_path = tmp_path / "data.csv"
    csv_path.write_text("name\na\nb\nc\n", encoding="utf-8")

    class GuardedRows:
        def __init__(self):
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index >= 2:
                raise AssertionError("CSV reader consumed beyond max_rows")
            self.index += 1
            return {"name": str(self.index)}

    monkeypatch.setattr(reporting.csv, "DictReader", lambda _file: GuardedRows())

    assert read_csv_rows(csv_path, max_rows=2) == [
        {"name": "1"},
        {"name": "2"},
    ]


def test_read_csv_rows_defines_zero_negative_and_empty_behavior(tmp_path):
    csv_path = tmp_path / "data.csv"
    csv_path.write_text("name\na\n", encoding="utf-8")
    empty_path = tmp_path / "empty.csv"
    empty_path.write_text("", encoding="utf-8")

    assert read_csv_rows(csv_path, max_rows=0) == []
    assert read_csv_rows(empty_path, max_rows=8) == []
    with pytest.raises(ValueError, match="nonnegative integer"):
        read_csv_rows(csv_path, max_rows=-1)
    with pytest.raises(TypeError, match="nonnegative integer"):
        read_csv_rows(csv_path, max_rows=1.5)


def test_format_markdown_table_handles_rows():
    rows = [
        {
            "name": "controller",
            "value": "stable",
        },
    ]

    table = format_markdown_table(
        rows,
        ["name", "value"],
    )

    assert "| name | value |" in table
    assert "| controller | stable |" in table


def test_markdown_table_cells_escape_pipes_and_line_breaks():
    assert escape_markdown_table_cell("alpha|beta") == r"alpha\|beta"
    assert escape_markdown_table_cell("first\r\nsecond\rthird") == (
        "first<br>second<br>third"
    )

    table = format_markdown_table(
        [{"name": "alpha|beta", "value": "first\nsecond"}],
        ["name", "value"],
    )
    assert table[-1] == r"| alpha\|beta | first<br>second |"


def test_generate_experiment_report_creates_file(tmp_path):
    results_dir = tmp_path / "results"
    results_dir.mkdir()
    output_path = tmp_path / "nested" / "reports" / "experiment_report.md"

    (results_dir / "performance_metrics.csv").write_text(
        "controller,initial_position,initial_velocity,final_state_norm,settling_time_s,quadratic_cost,control_energy,max_abs_control\n"
        "LQR,1.5,0.0,0.001,2.0,4.0,1.0,2.0\n",
        encoding="utf-8",
    )

    (results_dir / "stability_weight_ablation.csv").write_text(
        "stability_weight,decay_margin,derivative_violation_fraction,decay_margin_violation_fraction,max_vdot,max_decay_residual,final_state_norm,settling_time_s,quadratic_cost,control_energy\n"
        "10.0,0.05,0.0,0.01,-0.01,0.02,0.001,2.0,4.0,1.0\n",
        encoding="utf-8",
    )

    convergence_result = FiniteHorizonConvergenceResult(
        positions=np.array([-1.0, 0.0, 1.0]),
        velocities=np.array([-1.0, 0.0, 1.0]),
        convergence_map=np.ones((3, 3), dtype=bool),
        final_norm_map=np.zeros((3, 3)),
        horizon=8.0,
        convergence_tolerance=0.1,
        position_bounds=(-1.0, 1.0),
        velocity_bounds=(-1.0, 1.0),
        grid_resolution=3,
        tested_count=9,
        converged_count=9,
        convergence_fraction=1.0,
        controller_label="LQR",
    )

    generate_experiment_report(
        results_dir,
        output_path,
        finite_horizon_results={"LQR": convergence_result},
        experiment_seed_metadata={
            "Stability-weight ablation": {
                "base_seed": 700,
                "seed_list": "700;701;702",
                "repeat_count": 3,
                "pairing_strategy": "paired seeds across all stability weights",
            },
            "Measurement-noise robustness": {
                "base_seed": 7,
                "seed_list": "7;8;9",
                "repeat_count": 3,
                "pairing_strategy": (
                    "common random-number realizations across noise amplitudes"
                ),
            },
        },
        provenance={
            "run_id": "controlled-run",
            "source_commit": "a" * 40,
            "git_dirty": False,
            "generated_at_utc": "2026-08-08T01:02:03Z",
            "package_version": "1.0.1",
            "manifest": "manifest.json",
            "configuration_sha256": "b" * 64,
            "ablation_seeds": [700, 701, 702],
            "noise_seeds": [7, 8, 9],
            "repeat_count": 3,
            "pairing_strategies": ["paired", "common random numbers"],
            "decay_margin": 0.05,
            "finite_horizon": {"horizon": 8.0},
        },
    )

    text = output_path.read_text(encoding="utf-8")

    assert output_path.exists()
    assert "# Experiment Report" in text
    assert "Performance metrics preview" in text
    assert "Stability-weight ablation preview" in text
    assert "derivative_violation_fraction" in text
    assert "decay_margin_violation_fraction" in text
    assert "not a formal continuous-state certificate" in text
    assert "Finite-horizon convergence sampling" in text
    assert "Horizon (normalized time)" in text
    assert "integrated_squared_control_effort" in text
    assert "||x(T)||_2 < tolerance" in text
    assert (
        "8 | 0.1 | (-1.0, 1.0) | (-1.0, 1.0) | 3 x 3 | "
        "9 / 9 | 100.0%"
    ) in text
    assert "Region of attraction" not in text
    assert "ROA" not in text
    assert "Experimental seed design" in text
    assert "700;701;702" in text
    assert "paired seeds across all stability weights" in text
    assert "common random-number realizations across noise amplitudes" in text
    assert "do not guarantee fully deterministic execution" in text
    assert "## Run provenance" in text
    assert "controlled-run" in text
    assert "manifest.json" in text
    assert "/Users/" not in text


def test_report_marks_legacy_ablation_schema_as_ambiguous(tmp_path):
    results_dir = tmp_path / "results"
    results_dir.mkdir()
    (results_dir / "stability_weight_ablation.csv").write_text(
        "stability_weight,lyapunov_violation_fraction\n10.0,0.0\n",
        encoding="utf-8",
    )
    output_path = tmp_path / "report.md"

    generate_experiment_report(results_dir, output_path)

    assert "legacy ambiguous violation column" in output_path.read_text(
        encoding="utf-8"
    )


def test_report_reads_only_the_explicit_run_directory(tmp_path):
    first = tmp_path / "run-one"
    second = tmp_path / "run-two"
    first.mkdir()
    second.mkdir()
    for directory, value in ((first, "0.111"), (second, "9.999")):
        (directory / "performance_metrics.csv").write_text(
            "controller,final_state_norm\n" f"LQR,{value}\n",
            encoding="utf-8",
        )

    generate_experiment_report(first, first / "report.md")
    text = (first / "report.md").read_text(encoding="utf-8")
    assert "0.111" in text
    assert "9.999" not in text
