from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "project_status.py"

spec = importlib.util.spec_from_file_location("project_status", SCRIPT_PATH)
project_status = importlib.util.module_from_spec(spec)
assert spec is not None
assert spec.loader is not None
spec.loader.exec_module(project_status)


def test_count_files_returns_zero_for_missing_directory(tmp_path):
    assert project_status.count_files(tmp_path / "missing") == 0


def test_count_files_counts_matching_files(tmp_path):
    docs_dir = tmp_path / "docs"
    nested_dir = docs_dir / "nested"
    nested_dir.mkdir(parents=True)
    (docs_dir / "index.md").write_text("# Docs\n", encoding="utf-8")
    (nested_dir / "guide.md").write_text("# Guide\n", encoding="utf-8")
    (docs_dir / "notes.txt").write_text("notes\n", encoding="utf-8")

    assert project_status.count_files(docs_dir, "*.md") == 2


def test_status_label_reports_ok_and_missing(tmp_path):
    existing = tmp_path / "README.md"
    existing.write_text("# Project\n", encoding="utf-8")

    assert project_status.status_label(existing) == "OK"
    assert project_status.status_label(tmp_path / "missing.md") == "MISSING"


def test_main_returns_zero_when_key_files_exist(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    for file_name in project_status.KEY_FILES:
        path = Path(file_name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("placeholder\n", encoding="utf-8")

    assert project_status.main() == 0


def test_main_returns_one_when_key_files_are_missing(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert project_status.main() == 1
