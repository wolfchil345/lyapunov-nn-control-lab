"""Check every repository Markdown link, image target, and local anchor."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", ".pytest_cache", ".venv", "__pycache__"}
IGNORED_SUFFIXES = {".egg-info"}


def is_ignored(path: Path, root: Path) -> bool:
    """Return whether a generated or environment path should be skipped."""

    relative = path.relative_to(root)
    return any(
        part in IGNORED_PARTS
        or any(part.endswith(suffix) for suffix in IGNORED_SUFFIXES)
        for part in relative.parts
    )


def is_external_link(target: str) -> bool:
    """Return whether a link uses an external or non-file scheme."""

    stripped = target.strip()
    if stripped.startswith("//"):
        return True
    scheme = urlsplit(stripped).scheme.lower()
    return bool(scheme) and scheme not in {"file"}


def split_target(target: str) -> tuple[str, str]:
    """Return a decoded local path and anchor from a Markdown target."""

    cleaned = target.strip()
    if cleaned.startswith("<") and cleaned.endswith(">"):
        cleaned = cleaned[1:-1].strip()
    path_and_query, separator, anchor = cleaned.partition("#")
    path_text = path_and_query.split("?", 1)[0].strip()
    return unquote(path_text), unquote(anchor) if separator else ""


def github_heading_slug(heading: str) -> str:
    """Approximate GitHub's Unicode-aware Markdown heading slug."""

    heading = re.sub(r"<[^>]+>", "", heading)
    heading = re.sub(r"[`*_~]", "", heading)
    heading = re.sub(r"[^\w\- ]", "", heading.lower(), flags=re.UNICODE)
    return re.sub(r"\s+", "-", heading.strip())


def heading_anchors(path: Path) -> set[str]:
    """Return GitHub-style anchors, including duplicate-heading suffixes."""

    text = path.read_text(encoding="utf-8")
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for match in HEADING_PATTERN.finditer(text):
        base = github_heading_slug(match.group(1))
        count = counts.get(base, 0)
        anchor = base if count == 0 else f"{base}-{count}"
        counts[base] = count + 1
        anchors.add(anchor)
    return anchors


def markdown_files(root: Path = ROOT) -> list[Path]:
    """Return every user-facing Markdown file in the repository."""

    return sorted(
        path
        for path in root.rglob("*.md")
        if path.is_file() and not is_ignored(path, root)
    )


def resolve_target(path: Path, target_text: str, root: Path) -> Path:
    """Resolve a repository-relative or document-relative local target."""

    if not target_text:
        return path.resolve()
    if target_text.startswith("/"):
        return (root / target_text.lstrip("/")).resolve()
    return (path.parent / target_text).resolve()


def check_file(path: Path, root: Path = ROOT) -> list[str]:
    """Return missing-target and missing-anchor messages for one file."""

    text = path.read_text(encoding="utf-8")
    problems = []

    for match in LINK_PATTERN.finditer(text):
        raw_target = match.group(1)
        if is_external_link(raw_target):
            continue

        target_text, anchor = split_target(raw_target)
        target_path = resolve_target(path, target_text, root)
        line_number = text.count("\n", 0, match.start()) + 1
        relative_path = path.relative_to(root)

        try:
            target_path.relative_to(root.resolve())
        except ValueError:
            problems.append(
                f"{relative_path}:{line_number}: target leaves repository: {raw_target}",
            )
            continue

        if not target_path.exists():
            problems.append(f"{relative_path}:{line_number}: missing {raw_target}")
            continue

        if anchor and target_path.is_file() and target_path.suffix.lower() == ".md":
            if anchor not in heading_anchors(target_path):
                problems.append(
                    f"{relative_path}:{line_number}: missing anchor #{anchor} in "
                    f"{target_path.relative_to(root)}",
                )

    return problems


def main() -> None:
    """Check all repository Markdown links and local assets."""

    files = markdown_files()
    problems = []
    for path in files:
        problems.extend(check_file(path))

    if problems:
        print("Invalid local Markdown links:")
        for problem in problems:
            print(f"- {problem}")
        raise SystemExit(1)

    print(f"All local Markdown links are valid ({len(files)} files checked).")


if __name__ == "__main__":
    sys.exit(main())
