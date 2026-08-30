#!/usr/bin/env python3
"""Objective structural i18n parity checker.

This checker validates mechanically testable repository invariants only. It does
not attempt to prove translation quality.

Usage:
  python scripts/check_docs_i18n_parity.py
  python scripts/check_docs_i18n_parity.py --repo-root /path/to/repo
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_MARKERS = (
    "placeholder localized file",
    "translation pending",
    "not yet translated",
    "todo_translation",
    "tbd_translation",
)

REQUIRED_ROOT_FAMILIES = (
    "README",
    "CONTRIBUTING",
    "ROADMAP",
    "RELEASE_NOTES",
    "SECURITY",
    "CODE_OF_CONDUCT",
)

ISSUE_TEMPLATE_FAMILIES = (
    "bug_report",
    "experiment_suggestion",
)
ISSUE_TEMPLATE_LANG_SUFFIXES = ("", ".ja", ".ko", ".th")
ISSUE_TEMPLATE_REQUIRED_KEYS = (
    "name",
    "about",
    "title",
    "labels",
    "assignees",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Path to repository root (defaults to script parent root).",
    )
    return parser.parse_args()


def md_files(folder: Path) -> set[str]:
    if not folder.exists():
        return set()
    return {p.name for p in folder.glob("*.md") if p.is_file()}


def read_text(path: Path, failures: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:  # pragma: no cover - defensive
        failures.append(f"UNREADABLE: {path} ({exc})")
        return ""


def ensure_non_empty(path: Path, failures: list[str], context: str) -> str:
    if not path.exists():
        failures.append(f"MISSING: {context} -> {path}")
        return ""
    text = read_text(path, failures)
    if text.strip() == "":
        failures.append(f"EMPTY: {context} -> {path}")
    return text


def has_explicit_placeholder_marker(text: str) -> str | None:
    lower = text.lower()
    for marker in PLACEHOLDER_MARKERS:
        if marker in lower:
            return marker
    return None


def iter_markdown_targets(text: str) -> Iterable[str]:
    for raw in LINK_RE.findall(text):
        target = raw.strip()
        if not target:
            continue
        if target.startswith("#"):
            continue
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
            continue
        yield target.split("#", 1)[0].split("?", 1)[0]


def resolves_link_to(source: Path, text: str, expected_abs: Path) -> bool:
    expected_norm = expected_abs.resolve()
    for target in iter_markdown_targets(text):
        resolved = (source.parent / target).resolve()
        if resolved == expected_norm:
            return True
    return False


def parse_frontmatter(text: str) -> dict[str, str] | None:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return None
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        return None
    out: dict[str, str] = {}
    for line in lines[1:end_idx]:
        if line.strip() == "":
            continue
        if ":" not in line:
            return None
        key, value = line.split(":", 1)
        key = key.strip()
        if not key:
            return None
        out[key] = value.strip()
    return out


def check_docs_parity(repo_root: Path, failures: list[str]) -> None:
    docs = repo_root / "docs"
    lang_dirs = {
        "en": docs / "en",
        "ja": docs / "ja",
        "ko": docs / "ko",
        "th": docs / "th",
    }

    for lang, folder in lang_dirs.items():
        if not folder.exists():
            failures.append(f"MISSING DIR: docs/{lang}")

    en_set = md_files(lang_dirs["en"])
    if not en_set:
        failures.append("EMPTY OR MISSING: docs/en has no markdown files")
        return

    for lang in ("ja", "ko", "th"):
        lang_set = md_files(lang_dirs[lang])
        missing = sorted(en_set - lang_set)
        orphan = sorted(lang_set - en_set)
        for name in missing:
            failures.append(f"MISSING: docs/{lang}/{name} (counterpart to docs/en/{name})")
        for name in orphan:
            failures.append(f"ORPHAN: docs/{lang}/{name} has no docs/en counterpart")

    # Validate all maintained docs pages (en/ja/ko/th): non-empty, marker-free,
    # and four-language navigation links that resolve to sibling language pages.
    for name in sorted(en_set):
        expected_targets = {
            "en": lang_dirs["en"] / name,
            "ja": lang_dirs["ja"] / name,
            "ko": lang_dirs["ko"] / name,
            "th": lang_dirs["th"] / name,
        }
        for lang, path in expected_targets.items():
            text = ensure_non_empty(path, failures, f"maintained docs page docs/{lang}/{name}")
            if not text:
                continue
            marker = has_explicit_placeholder_marker(text)
            if marker is not None:
                failures.append(f"PLACEHOLDER MARKER: docs/{lang}/{name} contains '{marker}'")
            for check_lang, expected_abs in expected_targets.items():
                if not resolves_link_to(path, text, expected_abs):
                    failures.append(
                        "MISSING LANGUAGE NAV LINK: "
                        f"docs/{lang}/{name} does not link to docs/{check_lang}/{name}"
                    )


def check_root_routers(repo_root: Path, failures: list[str]) -> None:
    docs = repo_root / "docs"
    en_dir = docs / "en"
    for root_file in sorted(p for p in docs.glob("*.md") if (en_dir / p.name).exists()):
        text = ensure_non_empty(root_file, failures, f"root compatibility router docs/{root_file.name}")
        if not text:
            continue
        marker = has_explicit_placeholder_marker(text)
        if marker is not None:
            failures.append(f"PLACEHOLDER MARKER: docs/{root_file.name} contains '{marker}'")

        expected = {
            "en": docs / "en" / root_file.name,
            "ja": docs / "ja" / root_file.name,
            "ko": docs / "ko" / root_file.name,
            "th": docs / "th" / root_file.name,
        }
        for lang, expected_abs in expected.items():
            if not resolves_link_to(root_file, text, expected_abs):
                failures.append(
                    "MALFORMED ROUTER: "
                    f"docs/{root_file.name} missing link to docs/{lang}/{root_file.name}"
                )


def check_required_root_families(repo_root: Path, failures: list[str]) -> None:
    suffixes = {
        "en": ".md",
        "ja": ".ja.md",
        "ko": ".ko.md",
        "th": ".th.md",
    }
    for base in REQUIRED_ROOT_FAMILIES:
        files = {lang: repo_root / f"{base}{suf}" for lang, suf in suffixes.items()}
        for lang, path in files.items():
            text = ensure_non_empty(path, failures, f"required root family file {path.name}")
            if not text:
                continue
            marker = has_explicit_placeholder_marker(text)
            if marker is not None:
                failures.append(f"PLACEHOLDER MARKER: {path.name} contains '{marker}'")
            for check_lang, expected_path in files.items():
                if not resolves_link_to(path, text, expected_path):
                    failures.append(
                        "MISSING ROOT FAMILY NAV LINK: "
                        f"{path.name} does not link to {expected_path.name}"
                    )


def check_issue_templates(repo_root: Path, failures: list[str]) -> None:
    issue_dir = repo_root / ".github" / "ISSUE_TEMPLATE"
    if not issue_dir.exists():
        failures.append("MISSING DIR: .github/ISSUE_TEMPLATE")
        return

    for base in ISSUE_TEMPLATE_FAMILIES:
        for suffix in ISSUE_TEMPLATE_LANG_SUFFIXES:
            rel = f"{base}{suffix}.md"
            path = issue_dir / rel
            text = ensure_non_empty(path, failures, f"issue template {path}")
            if not text:
                continue
            marker = has_explicit_placeholder_marker(text)
            if marker is not None:
                failures.append(f"PLACEHOLDER MARKER: {path} contains '{marker}'")
            frontmatter = parse_frontmatter(text)
            if frontmatter is None:
                failures.append(f"INVALID FRONTMATTER: {path} must have '---' delimiters and key: value entries")
                continue
            for key in ISSUE_TEMPLATE_REQUIRED_KEYS:
                if key not in frontmatter:
                    failures.append(f"MISSING FRONTMATTER KEY: {path} missing '{key}'")


def check_pr_templates(repo_root: Path, failures: list[str]) -> None:
    root_template = repo_root / ".github" / "pull_request_template.md"
    ensure_non_empty(root_template, failures, f"PR template {root_template}")

    locale_dir = repo_root / ".github" / "PULL_REQUEST_TEMPLATE"
    for lang in ("ja", "ko", "th"):
        path = locale_dir / f"pull_request_template.{lang}.md"
        ensure_non_empty(path, failures, f"PR template {path}")

    for lang in ("ja", "ko", "th"):
        obsolete = repo_root / ".github" / f"pull_request_template.{lang}.md"
        if obsolete.exists():
            failures.append(f"OBSOLETE PR TEMPLATE LOCATION: {obsolete} should not exist")


def run(repo_root: Path) -> int:
    failures: list[str] = []
    check_docs_parity(repo_root, failures)
    check_root_routers(repo_root, failures)
    check_required_root_families(repo_root, failures)
    check_issue_templates(repo_root, failures)
    check_pr_templates(repo_root, failures)

    if failures:
        print("i18n parity check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        print(f"Total failures: {len(failures)}", file=sys.stderr)
        return 1

    print("i18n parity check passed: structural four-language invariants satisfied.")
    return 0


def main() -> int:
    args = parse_args()
    repo_root = (
        Path(args.repo_root).resolve()
        if args.repo_root
        else Path(__file__).resolve().parents[1]
    )
    return run(repo_root)


if __name__ == "__main__":
    raise SystemExit(main())
