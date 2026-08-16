"""Check local Markdown links in project documentation."""

from __future__ import annotations

import re
import sys
from pathlib import Path


LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ROOT = Path(__file__).resolve().parents[1]


def is_external_link(target: str) -> bool:
    """Return True if the link should not be checked as a local file."""
    return target.startswith(("http://", "https://", "mailto:", "#"))


def clean_target(target: str) -> str:
    """Remove anchors, query strings, and optional angle brackets."""
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    target = target.split("#", 1)[0]
    target = target.split("?", 1)[0]
    return target.strip()


def markdown_files() -> list[Path]:
    """Return Markdown files that should be checked."""
    files = []
    # Root README
    readme = ROOT / "README.md"
    if readme.exists():
        files.append(readme)

    # results README
    results_readme = ROOT / "results" / "README.md"
    if results_readme.exists():
        files.append(results_readme)

    # All markdown under docs/ recursively and localized subdirectories
    docs_dir = ROOT / "docs"
    if docs_dir.exists():
        files.extend(sorted(p for p in docs_dir.rglob("*.md") if p.is_file()))

    # Workflow and repo-level markdown (e.g., .github/*.md)
    workflows_md = ROOT / ".github"
    if workflows_md.exists():
        files.extend(sorted(p for p in workflows_md.rglob("*.md") if p.is_file()))

    # Deduplicate while preserving order
    seen = set()
    out: list[Path] = []
    for p in files:
        rp = p.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        # Exclude vendor, build, virtualenv, and git directories
        parts = set(p.parts)
        if {".git", ".venv", "venv", "build", "dist", "tmp", "__pycache__"} & parts:
            continue
        out.append(p)
    return out


def check_file(path: Path) -> list[str]:
    """Return missing-link messages for one Markdown file."""
    text = path.read_text(encoding="utf-8")
    problems = []

    for match in LINK_PATTERN.finditer(text):
        raw_target = match.group(1)
        if is_external_link(raw_target):
            continue

        target_text = clean_target(raw_target)
        if not target_text or is_external_link(target_text):
            continue

        target_path = (path.parent / target_text).resolve()
        try:
            target_path.relative_to(ROOT)
        except ValueError:
            continue

        if not target_path.exists():
            line_number = text.count("\n", 0, match.start()) + 1
            relative_path = path.relative_to(ROOT)
            problems.append(f"{relative_path}:{line_number}: missing {raw_target}")

    return problems


def main() -> None:
    """Check all documentation links."""
    problems = []
    for path in markdown_files():
        problems.extend(check_file(path))

    if problems:
        print("Missing local Markdown links:")
        for problem in problems:
            print(f"- {problem}")
        raise SystemExit(1)

    print("All local Markdown links are valid.")


if __name__ == "__main__":
    main()
