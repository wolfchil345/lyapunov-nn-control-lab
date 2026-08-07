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
