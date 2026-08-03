"""Create a timestamped experiment log from a localized template."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


SUPPORTED_LANGUAGES = ("en", "ja", "ko", "th")


def slugify(text: str) -> str:
    """Return a safe English filename component."""

    slug = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
    return slug or "experiment"


def create_log(title: str = "experiment", language: str = "en") -> Path:
    """Copy one localized template to a timestamped result file."""

    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Unsupported language: {language}")

    template_path = Path("docs") / language / "experiment_log_template.md"
    if not template_path.exists():
        raise FileNotFoundError(f"Missing {template_path}")

    output_dir = Path("results/experiment_logs")
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    language_suffix = "" if language == "en" else f".{language}"
    output_path = output_dir / f"{timestamp}_{slugify(title)}{language_suffix}.md"
    content = template_path.read_text(encoding="utf-8")
    output_path.write_text(content, encoding="utf-8")
    return output_path


def parse_args() -> argparse.Namespace:
    """Parse the log title and localized template choice."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", nargs="*", help="Short English filename label")
    parser.add_argument(
        "--language",
        choices=SUPPORTED_LANGUAGES,
        default="en",
        help="Template language (default: en)",
    )
    return parser.parse_args()


def main() -> int:
    """Create one experiment log and print its path."""

    args = parse_args()
    title = " ".join(args.title) if args.title else "experiment"
    output_path = create_log(title, language=args.language)
    print(f"Created experiment log: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
