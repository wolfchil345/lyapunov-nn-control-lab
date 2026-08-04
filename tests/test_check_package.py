from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "check_package.py"

spec = importlib.util.spec_from_file_location("check_package", SCRIPT_PATH)
check_package = importlib.util.module_from_spec(spec)
assert spec is not None
assert spec.loader is not None
spec.loader.exec_module(check_package)


def test_declared_version_reads_project_version(tmp_path):
    project = tmp_path / "pyproject.toml"
    project.write_text('[project]\nversion = "2.3.4"\n', encoding="utf-8")

    assert check_package.declared_version(project) == "2.3.4"


def test_declared_version_rejects_missing_version(tmp_path):
    project = tmp_path / "pyproject.toml"
    project.write_text("[project]\n", encoding="utf-8")

    with pytest.raises(ValueError, match="No project version"):
        check_package.declared_version(project)


def test_requirement_name_normalizes_supported_forms():
    assert check_package.requirement_name("NumPy>=2") == "numpy"
    assert check_package.requirement_name("typing_extensions; python_version<'3.11'") == (
        "typing-extensions"
    )


def test_repository_package_metadata_is_valid():
    assert check_package.audit_package() == []
