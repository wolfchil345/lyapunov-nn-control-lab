from __future__ import annotations

from pathlib import Path

REQUIRED_WORKFLOW_BADGES = [
    "tests.yml",
    "quality-gate.yml",
]

README_FILES = [
    Path("README.md"),
    Path("README.ja.md"),
    Path("README.ko.md"),
    Path("README.th.md"),
]


def main() -> int:
    workflows_dir = Path(".github/workflows")
    missing = []

    readme_text: dict[Path, str] = {}
    for readme in README_FILES:
        if not readme.exists():
            missing.append(f"Missing {readme}")
            continue
        readme_text[readme] = readme.read_text(encoding="utf-8")

    for workflow_name in REQUIRED_WORKFLOW_BADGES:
        workflow_path = workflows_dir / workflow_name
        badge_text = f"actions/workflows/{workflow_name}/badge.svg"

        if not workflow_path.exists():
            missing.append(f"Missing workflow file: {workflow_path}")

        for readme, text in readme_text.items():
            if badge_text not in text:
                missing.append(
                    f"{readme}: Missing README badge for: {workflow_name}"
                )

    if missing:
        print("Workflow badge check failed:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("Workflow badges look good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
