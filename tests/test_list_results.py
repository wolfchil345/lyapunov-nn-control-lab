from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "list_results.py"

spec = importlib.util.spec_from_file_location("list_results", SCRIPT_PATH)
list_results = importlib.util.module_from_spec(spec)
assert spec is not None
assert spec.loader is not None
spec.loader.exec_module(list_results)


def test_format_size_bytes():
    assert list_results.format_size(512) == "512 B"


def test_format_size_kilobytes():
    assert list_results.format_size(2048) == "2.0 KB"


def test_format_size_megabytes():
    assert list_results.format_size(2 * 1024 * 1024) == "2.0 MB"


def test_list_result_files_returns_only_files(tmp_path):
    results_dir = tmp_path / "results"
    nested_dir = results_dir / "nested"
    nested_dir.mkdir(parents=True)

    first_file = results_dir / "metrics.csv"
    second_file = nested_dir / "plot.png"
    first_file.write_text("metric,value\n", encoding="utf-8")
    second_file.write_text("fake image text\n", encoding="utf-8")

    files = list_results.list_result_files(results_dir)

    assert first_file in files
    assert second_file in files
    assert nested_dir not in files
    assert len(files) == 2


def test_list_result_files_missing_directory(tmp_path):
    missing_dir = tmp_path / "missing_results"
    assert list_results.list_result_files(missing_dir) == []
