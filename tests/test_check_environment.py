from __future__ import annotations

import importlib.util
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "check_environment.py"

spec = importlib.util.spec_from_file_location("check_environment", SCRIPT_PATH)
check_environment = importlib.util.module_from_spec(spec)
assert spec is not None
assert spec.loader is not None
spec.loader.exec_module(check_environment)


def test_runtime_imports_match_project_dependencies():
    module_names = {name for name, _label in check_environment.RUNTIME_IMPORTS}

    assert module_names == {
        "control",
        "lyapunov_nn_control_lab",
        "matplotlib",
        "numpy",
        "scipy",
        "torch",
    }


def test_check_import_reports_success(monkeypatch, capsys):
    module = SimpleNamespace(__version__="1.2.3")
    monkeypatch.setattr(check_environment.importlib, "import_module", lambda _name: module)

    assert check_environment.check_import("example", "Example")
    assert "PASS: Example import works: 1.2.3" in capsys.readouterr().out


def test_check_import_reports_failure(monkeypatch, capsys):
    def fail_import(_name):
        raise ImportError("not installed")

    monkeypatch.setattr(check_environment.importlib, "import_module", fail_import)

    assert not check_environment.check_import("example", "Example")
    assert "FAIL: Example import failed: not installed" in capsys.readouterr().out
