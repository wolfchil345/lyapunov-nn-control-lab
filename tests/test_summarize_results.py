from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "summarize_results.py"

spec = importlib.util.spec_from_file_location("summarize_results", SCRIPT_PATH)
summarize_results = importlib.util.module_from_spec(spec)
assert spec is not None
assert spec.loader is not None
spec.loader.exec_module(summarize_results)


def test_ablation_summary_names_both_violation_metrics(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(summarize_results, "RESULTS_DIR", tmp_path)
    (tmp_path / "stability_weight_ablation.csv").write_text(
        "stability_weight,decay_margin,derivative_violation_fraction,decay_margin_violation_fraction,final_state_norm\n"
        "10.0,0.05,0.0,0.1,0.001\n",
        encoding="utf-8",
    )

    summarize_results.print_ablation_metrics()

    output = capsys.readouterr().out
    assert "derivative_violation=0.0" in output
    assert "margin_violation(alpha=0.05)=0.1" in output


def test_ablation_summary_marks_historical_column_as_ambiguous(
    tmp_path,
    monkeypatch,
    capsys,
):
    monkeypatch.setattr(summarize_results, "RESULTS_DIR", tmp_path)
    (tmp_path / "stability_weight_ablation.csv").write_text(
        "stability_weight,lyapunov_violation_fraction,final_state_norm\n"
        "10.0,0.0,0.001\n",
        encoding="utf-8",
    )

    summarize_results.print_ablation_metrics()

    assert "legacy_ambiguous_violation=0.0" in capsys.readouterr().out


def test_paired_aggregate_summaries_take_precedence(
    tmp_path,
    monkeypatch,
    capsys,
):
    monkeypatch.setattr(summarize_results, "RESULTS_DIR", tmp_path)
    (tmp_path / "stability_weight_ablation_summary_paired.csv").write_text(
        "stability_weight,n,final_state_norm_mean,final_state_norm_sample_std,derivative_violation_fraction_mean,decay_margin_violation_fraction_mean\n"
        "10.0,3,0.01,0.002,0.0,0.1\n",
        encoding="utf-8",
    )
    (tmp_path / "stability_weight_ablation.csv").write_text(
        "stability_weight,lyapunov_violation_fraction\n10.0,0.9\n",
        encoding="utf-8",
    )
    (tmp_path / "noise_robustness_summary_paired.csv").write_text(
        "noise_std,n,final_state_norm_mean,final_state_norm_sample_std\n"
        "0.1,3,0.02,0.003\n",
        encoding="utf-8",
    )

    summarize_results.print_ablation_metrics()
    summarize_results.print_noise_metrics()

    output = capsys.readouterr().out
    assert "Paired stability-weight ablation aggregates" in output
    assert "final_norm_sample_std=0.002" in output
    assert "legacy_ambiguous_violation" not in output
    assert "Paired measurement-noise aggregates" in output
    assert "noise_std=0.1" in output
