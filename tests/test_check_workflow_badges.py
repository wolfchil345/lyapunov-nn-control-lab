from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "check_workflow_badges.py"

spec = importlib.util.spec_from_file_location("check_workflow_badges", SCRIPT_PATH)
check_workflow_badges = importlib.util.module_from_spec(spec)
assert spec is not None
assert spec.loader is not None
spec.loader.exec_module(check_workflow_badges)


def write_workflows(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "tests.yml").write_text("name: Python tests\n", encoding="utf-8")
    (workflows / "quality-gate.yml").write_text("name: Quality gate\n", encoding="utf-8")


def write_readme(tmp_path: Path, *, include_quality_gate: bool = True) -> None:
    lines = [
        "![Python tests](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml/badge.svg)",
    ]

    if include_quality_gate:
        lines.append(
            "![Quality gate](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml/badge.svg)"
        )

    lines.append("# Lyapunov NN Control Lab")
    (tmp_path / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_main_passes_when_required_badges_exist(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_workflows(tmp_path)
    write_readme(tmp_path)

    assert check_workflow_badges.main() == 0
    assert "Workflow badges look good." in capsys.readouterr().out


def test_main_fails_when_readme_is_missing(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_workflows(tmp_path)

    assert check_workflow_badges.main() == 1
    assert "Missing README.md" in capsys.readouterr().out


def test_main_fails_when_quality_gate_badge_is_missing(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    write_workflows(tmp_path)
    write_readme(tmp_path, include_quality_gate=False)

    assert check_workflow_badges.main() == 1
    assert "Missing README badge for: quality-gate.yml" in capsys.readouterr().out


def test_main_fails_when_workflow_file_is_missing(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    workflows = tmp_path / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "tests.yml").write_text("name: Python tests\n", encoding="utf-8")
    write_readme(tmp_path)

    assert check_workflow_badges.main() == 1
    assert "Missing workflow file: .github/workflows/quality-gate.yml" in capsys.readouterr().out
