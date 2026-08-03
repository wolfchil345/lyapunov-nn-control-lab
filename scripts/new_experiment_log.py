from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
    return slug or "experiment"


def create_log(title: str = "experiment") -> Path:
    template_path = Path("docs/experiment_log_template.md")
    if not template_path.exists():
        raise FileNotFoundError("Missing docs/experiment_log_template.md")

    output_dir = Path("results/experiment_logs")
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"{timestamp}_{slugify(title)}.md"
    content = template_path.read_text(encoding="utf-8")
    output_path.write_text(content, encoding="utf-8")
    return output_path


def main() -> int:
    title = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "experiment"
    output_path = create_log(title)
    print(f"Created experiment log: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
