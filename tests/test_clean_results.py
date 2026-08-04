from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "clean_results.py"

spec = importlib.util.spec_from_file_location("clean_results", SCRIPT_PATH)
clean_results = importlib.util.module_from_spec(spec)
assert spec is not None
assert spec.loader is not None
spec.loader.exec_module(clean_results)


def create_result_files(results_dir: Path) -> tuple[Path, Path, Path]:
    results_dir.mkdir()
    generated = results_dir / "training_loss.png"
    unknown = results_dir / "research_notes.md"
    nested = results_dir / "experiment_logs"
    nested.mkdir()
    generated.write_bytes(b"generated")
    unknown.write_text("keep me\n", encoding="utf-8")
    (nested / "log.md").write_text("keep me too\n", encoding="utf-8")
    return generated, unknown, nested


def test_cleanup_is_a_dry_run_by_default(tmp_path):
    generated, unknown, nested = create_result_files(tmp_path / "results")

    count = clean_results.clean_results(tmp_path / "results")

    assert count == 1
    assert generated.exists()
    assert unknown.exists()
    assert nested.exists()


def test_confirmed_cleanup_removes_only_known_generated_files(tmp_path):
    generated, unknown, nested = create_result_files(tmp_path / "results")

    count = clean_results.clean_results(tmp_path / "results", confirmed=True)

    assert count == 1
    assert not generated.exists()
    assert unknown.exists()
    assert (nested / "log.md").exists()


def test_cleanup_handles_missing_results_directory(tmp_path):
    assert clean_results.clean_results(tmp_path / "missing", confirmed=True) == 0
