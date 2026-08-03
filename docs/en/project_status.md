🌐 Language: [English](../en/project_status.md) | [日本語](../ja/project_status.md) | [한국어](../ko/project_status.md) | [ไทย](../th/project_status.md)

# Project Status

Run:

```bash
python scripts/project_status.py
```

The command checks key repository files and reports counts for documentation, scripts, tests, workflows, and result artifacts. It is an inventory check, not a substitute for tests or scientific review.

## When to use it

- After reorganizing files.
- Before a pull request, demo, or release.
- After adding documentation, scripts, tests, or workflows.

Update `KEY_FILES` in `scripts/project_status.py` when a new file becomes essential. The [quality gate](quality_gate.md) runs this status command as one part of a broader validation sequence.
