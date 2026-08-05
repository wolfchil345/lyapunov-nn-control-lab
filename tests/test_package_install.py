from __future__ import annotations

import os
from pathlib import Path
import site
import subprocess
import sys
import textwrap
import zipfile


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_NAME = "lyapunov_nn_control_lab"


def test_wheel_install_imports_from_outside_repository(tmp_path: Path) -> None:
    """Build and import the wheel without relying on the repository path."""
    wheel_dir = tmp_path / "wheelhouse"
    wheel_dir.mkdir()

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "wheel",
            "--no-deps",
            "--wheel-dir",
            str(wheel_dir),
            str(PROJECT_ROOT),
        ],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    wheels = list(wheel_dir.glob("*.whl"))
    assert len(wheels) == 1
    wheel = wheels[0]

    with zipfile.ZipFile(wheel) as archive:
        members = archive.namelist()

    python_members = [member for member in members if member.endswith(".py")]
    assert f"{PACKAGE_NAME}/__init__.py" in python_members
    assert all(member.startswith(f"{PACKAGE_NAME}/") for member in python_members)
    assert not any(
        member.startswith(("src/", "tests/", "results/", "docs/"))
        for member in members
    )

    venv_dir = tmp_path / "venv"
    subprocess.run(
        [sys.executable, "-m", "venv", str(venv_dir)],
        check=True,
    )
    venv_python = venv_dir / ("Scripts/python.exe" if os.name == "nt" else "bin/python")

    dependency_site = next(
        Path(directory)
        for directory in site.getsitepackages()
        if Path(directory).is_relative_to(Path(sys.prefix))
    )
    child_site = subprocess.run(
        [
            str(venv_python),
            "-c",
            "import site; print(site.getsitepackages()[0])",
        ],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    # Reuse the test environment's declared dependencies instead of reinstalling
    # large runtime wheels; the project wheel itself stays isolated below.
    dependency_path_file = Path(child_site) / "package-test-dependencies.pth"
    dependency_path_file.write_text(f"{dependency_site}\n", encoding="utf-8")

    subprocess.run(
        [
            str(venv_python),
            "-m",
            "pip",
            "install",
            "--no-deps",
            "--ignore-installed",
            str(wheel),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    outside_dir = tmp_path / "outside-repository"
    outside_dir.mkdir()
    import_check = textwrap.dedent(
        f"""
        from pathlib import Path
        import sys

        import {PACKAGE_NAME}
        import {PACKAGE_NAME}.controllers as controllers
        import {PACKAGE_NAME}.simulation as simulation
        import {PACKAGE_NAME}.system as system

        prefix = Path(sys.prefix).resolve()
        modules = ({PACKAGE_NAME}, controllers, simulation, system)
        for module in modules:
            module_path = Path(module.__file__).resolve()
            assert module_path.is_relative_to(prefix), (module.__name__, module_path, prefix)
        """
    )
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    environment["MPLBACKEND"] = "Agg"
    environment["MPLCONFIGDIR"] = str(tmp_path / "matplotlib")
    environment["PYTHONNOUSERSITE"] = "1"

    subprocess.run(
        [str(venv_python), "-c", import_check],
        cwd=outside_dir,
        env=environment,
        capture_output=True,
        text=True,
        check=True,
    )
