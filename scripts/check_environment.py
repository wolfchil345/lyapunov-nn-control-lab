from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def show(ok: bool, message: str) -> bool:
    label = "PASS" if ok else "FAIL"
    print(f"{label}: {message}")
    return ok


def check_python() -> bool:
    version = sys.version.split()[0]
    return show(sys.version_info >= (3, 10), f"Python version is {version}")


def check_command(command: str) -> bool:
    return show(shutil.which(command) is not None, f"`{command}` command is available")


def check_path(path: str) -> bool:
    return show(Path(path).exists(), f"`{path}` exists")


def check_git_lfs() -> bool:
    if shutil.which("git-lfs") is None:
        return show(False, "`git-lfs` command is available")
    result = subprocess.run(["git", "lfs", "version"], text=True, capture_output=True)
    ok = result.returncode == 0
    details = result.stdout.strip() or result.stderr.strip()
    return show(ok, f"Git LFS works: {details}")


def check_torch() -> bool:
    try:
        import torch
    except Exception as exc:
        return show(False, f"PyTorch import failed: {exc}")
    return show(True, f"PyTorch import works: {torch.__version__}")


def main() -> int:
    checks = [
        check_python(),
        check_command("git"),
        check_git_lfs(),
        check_path("README.md"),
        check_path("requirements.txt"),
        check_path("src"),
        check_path("tests"),
        check_path("scripts/run_checks.py"),
        check_torch(),
    ]
    if all(checks):
        print("Environment looks ready.")
        return 0
    print("Environment has problems. Check the FAIL lines above.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
