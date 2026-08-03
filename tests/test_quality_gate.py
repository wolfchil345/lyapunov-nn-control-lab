from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "quality_gate.py"

spec = importlib.util.spec_from_file_location("quality_gate", SCRIPT_PATH)
quality_gate = importlib.util.module_from_spec(spec)
assert spec is not None
assert spec.loader is not None
spec.loader.exec_module(quality_gate)


def test_run_command_returns_zero_for_success():
    result = quality_gate.run_command(["python", "-c", "import sys; sys.exit(0)"])
    assert result == 0


def test_run_command_returns_nonzero_for_failure():
    result = quality_gate.run_command(["python", "-c", "import sys; sys.exit(3)"])
    assert result == 3


def test_main_returns_zero_when_all_commands_pass(monkeypatch):
    monkeypatch.setattr(
        quality_gate,
        "COMMANDS",
        [[
            "python",
            "-c",
            "import sys; sys.exit(0)",
        ]],
    )

    assert quality_gate.main() == 0


def test_main_stops_when_command_fails(monkeypatch):
    monkeypatch.setattr(
        quality_gate,
        "COMMANDS",
        [
            ["python", "-c", "import sys; sys.exit(0)"],
            ["python", "-c", "import sys; sys.exit(4)"],
            ["python", "-c", "raise RuntimeError(\"should not run\")"],
        ],
    )

    assert quality_gate.main() == 4
