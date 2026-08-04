"""Validate installed package metadata and import layout."""

from __future__ import annotations

import re
from importlib import metadata
from pathlib import Path

PROJECT_NAME = "lyapunov-nn-control-lab"
PROJECT_FILE = Path("pyproject.toml")
VERSION_PATTERN = re.compile(r'^version\s*=\s*"([^"]+)"$', re.MULTILINE)
DEVELOPMENT_PACKAGES = {"pytest", "ruff"}


def declared_version(path: Path = PROJECT_FILE) -> str:
    """Return the version declared in pyproject.toml."""

    match = VERSION_PATTERN.search(path.read_text(encoding="utf-8"))
    if match is None:
        raise ValueError(f"No project version found in {path}")
    return match.group(1)


def requirement_name(requirement: str) -> str:
    """Return a normalized distribution name from a requirement string."""

    name = re.split(r"[<>=!~;\s\[]", requirement, maxsplit=1)[0]
    return name.lower().replace("_", "-")


def audit_package() -> list[str]:
    """Return package metadata and import-layout problems."""

    try:
        distribution = metadata.distribution(PROJECT_NAME)
    except metadata.PackageNotFoundError:
        return [f"{PROJECT_NAME} is not installed; run python -m pip install -e '.[dev]'"]

    problems = []
    expected_version = declared_version()
    if distribution.version != expected_version:
        problems.append(
            f"installed version {distribution.version} does not match "
            f"pyproject.toml version {expected_version}",
        )

    top_level = set((distribution.read_text("top_level.txt") or "").splitlines())
    if "src" not in top_level:
        problems.append("installed distribution does not expose the `src` package")

    runtime_requirements = {
        requirement_name(requirement)
        for requirement in distribution.requires or []
        if "extra ==" not in requirement
    }
    misplaced = sorted(DEVELOPMENT_PACKAGES & runtime_requirements)
    if misplaced:
        problems.append(
            "development-only packages listed as runtime dependencies: "
            + ", ".join(misplaced),
        )

    return problems


def main() -> int:
    """Print the package audit result."""

    problems = audit_package()
    if problems:
        print("Package check failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(
        f"Package metadata is valid ({PROJECT_NAME} {declared_version()}, import `src`).",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
