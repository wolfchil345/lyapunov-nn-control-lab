from __future__ import annotations

import importlib
import sys
from pathlib import Path


RUNTIME_IMPORTS = [
    ("control", "python-control"),
    ("matplotlib", "Matplotlib"),
    ("numpy", "NumPy"),
    ("scipy", "SciPy"),
    ("torch", "PyTorch"),
    ("lyapunov_nn_control_lab", "lyapunov-nn-control-lab"),
]

REQUIRED_PATHS = [
    "README.md",
    "pyproject.toml",
    "src/lyapunov_nn_control_lab",
    "tests",
    "scripts/run_checks.py",
]


def show(ok: bool, message: str) -> bool:
    label = "PASS" if ok else "FAIL"
    print(f"{label}: {message}")
    return ok


def check_python() -> bool:
    version = sys.version.split()[0]
    return show(sys.version_info >= (3, 10), f"Python version is {version}")


def check_path(path: str) -> bool:
    return show(Path(path).exists(), f"`{path}` exists")


def check_import(module_name: str, label: str) -> bool:
    try:
        module = importlib.import_module(module_name)
    except Exception as exc:
        return show(False, f"{label} import failed: {exc}")

    version = getattr(module, "__version__", None)
    details = f"{label} import works"
    if version is not None:
        details += f": {version}"
    return show(True, details)


def main() -> int:
    checks = [check_python()]
    checks.extend(check_path(path) for path in REQUIRED_PATHS)
    checks.extend(
        check_import(module_name, label)
        for module_name, label in RUNTIME_IMPORTS
    )
    if all(checks):
        print("Environment looks ready.")
        return 0
    print("Environment has problems. Check the FAIL lines above.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
