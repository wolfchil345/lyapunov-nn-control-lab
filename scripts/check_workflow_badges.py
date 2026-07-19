from __future__ import annotations

from pathlib import Path


REQUIRED_WORKFLOW_BADGES = [
    "tests.yml",
    "quality-gate.yml",
]


def main() -> int:
    readme = Path("README.md")
    workflows_dir = Path(".github/workflows")

    if not readme.exists():
        print("Missing README.md")
        return 1

    text = readme.read_text(encoding="utf-8")
    missing = []

    for workflow_name in REQUIRED_WORKFLOW_BADGES:
        workflow_path = workflows_dir / workflow_name
        badge_text = f"actions/workflows/{workflow_name}/badge.svg"

        if not workflow_path.exists():
            missing.append(f"Missing workflow file: {workflow_path}")

        if badge_text not in text:
            missing.append(f"Missing README badge for: {workflow_name}")

    if missing:
        print("Workflow badge check failed:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("Workflow badges look good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
