"""Validate four-language coverage and structure for user-facing Markdown."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("en", "ja", "ko", "th")
LANGUAGE_LABELS = ("[English]", "[日本語]", "[한국어]", "[ไทย]")
SCRIPT_PATTERNS = {
    "ja": re.compile(r"[ぁ-んァ-ン一-龯]"),
    "ko": re.compile(r"[가-힣]"),
    "th": re.compile(r"[ก-๙]"),
}
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
DUPLICATE_SUFFIX_PATTERN = re.compile(r" \d+\.(?:md|py)$")
TOP_LEVEL_FAMILIES = (
    "README",
    "CONTRIBUTING",
    "SECURITY",
    "CODE_OF_CONDUCT",
    "ROADMAP",
    "RELEASE_NOTES",
)


def localized_filename(stem: str, language: str) -> str:
    """Return the top-level filename for one language family."""

    return f"{stem}.md" if language == "en" else f"{stem}.{language}.md"


def heading_levels(path: Path) -> list[int]:
    """Return the ATX heading-level sequence in a document."""

    text = path.read_text(encoding="utf-8")
    return [
        len(match.group(1))
        for match in re.finditer(r"^(#{1,6})\s+", text, flags=re.MULTILINE)
    ]


def check_language_switcher(
    path: Path,
    family_paths: dict[str, Path],
) -> list[str]:
    """Check that the document header links the matching family in every language."""

    lines = path.read_text(encoding="utf-8").splitlines()
    header = "\n".join(lines[:15])
    problems = []
    missing = [label for label in LANGUAGE_LABELS if label not in header]
    if missing:
        problems.append(f"{path}: language switcher missing {', '.join(missing)}")

    linked_paths = {
        (path.parent / target.split("#", 1)[0]).resolve()
        for target in MARKDOWN_LINK_PATTERN.findall(header)
        if "://" not in target
    }
    for language, target in family_paths.items():
        if target.resolve() not in linked_paths:
            problems.append(
                f"{path}: language switcher has no {language} family link "
                f"to {target}",
            )
    return problems


def check_script_content(path: Path, language: str) -> list[str]:
    """Check that a localized file contains its language's writing system."""

    pattern = SCRIPT_PATTERNS.get(language)
    if pattern is None:
        return []
    text = path.read_text(encoding="utf-8")
    if not pattern.search(text):
        return [f"{path}: no {language} script content found"]
    return []


def check_family(paths: dict[str, Path], label: str) -> list[str]:
    """Check existence, switchers, scripts, and heading-structure parity."""

    problems = []
    missing = [language for language, path in paths.items() if not path.exists()]
    if missing:
        return [f"{label}: missing languages {', '.join(missing)}"]

    expected_levels = heading_levels(paths["en"])
    for language, path in paths.items():
        problems.extend(check_language_switcher(path, paths))
        problems.extend(check_script_content(path, language))
        actual_levels = heading_levels(path)
        if actual_levels != expected_levels:
            problems.append(
                f"{label}: {language} heading levels {actual_levels}; "
                f"English has {expected_levels}",
            )
    return problems


def check_index_coverage(index_path: Path, expected_names: set[str]) -> list[str]:
    """Check that one localized index links every document in its language tree."""

    if not index_path.exists():
        return [f"{index_path}: missing index file"]

    text = index_path.read_text(encoding="utf-8")
    targets = {
        target.split("#", 1)[0]
        for target in MARKDOWN_LINK_PATTERN.findall(text)
        if "/" not in target and target.endswith(".md")
    }
    required = expected_names - {"index.md"}
    missing = sorted(required - targets)
    if missing:
        return [f"{index_path}: missing index entries {', '.join(missing)}"]
    return []


def duplicate_suffix_files(root: Path) -> list[Path]:
    """Return sync-conflict-style duplicate Markdown or Python files."""

    ignored_parts = {".git", ".pytest_cache", ".venv", "__pycache__"}
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and DUPLICATE_SUFFIX_PATTERN.search(path.name)
        and not any(
            part in ignored_parts or part.endswith(".egg-info")
            for part in path.relative_to(root).parts
        )
    )


def audit_repository(root: Path = ROOT) -> list[str]:
    """Return every multilingual coverage problem in the repository."""

    problems = []
    docs = root / "docs"
    doc_names = {
        language: {path.name for path in (docs / language).glob("*.md")}
        for language in LANGUAGES
    }
    expected_names = doc_names["en"]

    for language in LANGUAGES[1:]:
        missing = sorted(expected_names - doc_names[language])
        extra = sorted(doc_names[language] - expected_names)
        if missing:
            problems.append(f"docs/{language}: missing {', '.join(missing)}")
        if extra:
            problems.append(f"docs/{language}: extra {', '.join(extra)}")

    for name in sorted(expected_names):
        paths = {language: docs / language / name for language in LANGUAGES}
        problems.extend(check_family(paths, f"docs/{name}"))

    for language in LANGUAGES:
        problems.extend(
            check_index_coverage(docs / language / "index.md", expected_names),
        )

    for stem in TOP_LEVEL_FAMILIES:
        paths = {
            language: root / localized_filename(stem, language)
            for language in LANGUAGES
        }
        problems.extend(check_family(paths, stem))

    report_paths = {
        "en": root / "results" / "experiment_report.md",
        "ja": root / "results" / "experiment_report.ja.md",
        "ko": root / "results" / "experiment_report.ko.md",
        "th": root / "results" / "experiment_report.th.md",
    }
    problems.extend(check_family(report_paths, "experiment report"))

    issue_templates = ("bug_report", "experiment_suggestion")
    for stem in issue_templates:
        paths = {
            language: root
            / ".github"
            / "ISSUE_TEMPLATE"
            / localized_filename(stem, language)
            for language in LANGUAGES
        }
        problems.extend(check_family(paths, f"issue template {stem}"))

    pr_paths = {
        "en": root / ".github" / "pull_request_template.md",
        "ja": root
        / ".github"
        / "PULL_REQUEST_TEMPLATE"
        / "pull_request_template.ja.md",
        "ko": root
        / ".github"
        / "PULL_REQUEST_TEMPLATE"
        / "pull_request_template.ko.md",
        "th": root
        / ".github"
        / "PULL_REQUEST_TEMPLATE"
        / "pull_request_template.th.md",
    }
    problems.extend(check_family(pr_paths, "pull request template"))

    for path in sorted(docs.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for language in LANGUAGES:
            target = f"{language}/{path.name}"
            if target not in text:
                problems.append(f"{path}: missing compatibility link {target}")

    for path in duplicate_suffix_files(root):
        problems.append(f"{path}: duplicate numeric suffix file")

    return problems


def main() -> int:
    """Print the multilingual documentation audit result."""

    problems = audit_repository()
    if problems:
        print("Multilingual documentation check failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    count = len(list((ROOT / "docs" / "en").glob("*.md")))
    print(
        "Multilingual documentation is complete: "
        f"{count} documentation families plus repository templates and reports.",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
