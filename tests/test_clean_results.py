from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "clean_results.py"
spec = importlib.util.spec_from_file_location("clean_results", SCRIPT_PATH)
clean_results = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(clean_results)


def test_cleanup_preserves_completed_runs_and_legacy_artifacts(tmp_path):
    results = tmp_path / "results"
    runs = results / "runs"
    complete = runs / "complete-run"
    staging = runs / ".staging-failed-run-12345678"
    complete.mkdir(parents=True)
    staging.mkdir()
    legacy = results / "historical.png"
    legacy.write_bytes(b"legacy")
    (complete / "manifest.json").write_text("{}", encoding="utf-8")
    (staging / "partial.csv").write_text("partial", encoding="utf-8")

    assert clean_results.clean_incomplete_staging(results) == 1
    assert complete.exists()
    assert legacy.read_bytes() == b"legacy"
    assert not staging.exists()


def test_cleanup_does_not_follow_staging_symlink(tmp_path):
    results = tmp_path / "results"
    runs = results / "runs"
    outside = tmp_path / "outside"
    outside.mkdir()
    runs.mkdir(parents=True)
    link = runs / ".staging-linked"
    try:
        link.symlink_to(outside, target_is_directory=True)
    except OSError:
        return

    assert clean_results.clean_incomplete_staging(results) == 0
    assert outside.exists()
