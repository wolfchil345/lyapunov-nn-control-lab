🌐 Language: [English](../en/maintenance.md) | [日本語](../ja/maintenance.md) | [한국어](../ko/maintenance.md) | [ไทย](../th/maintenance.md)

# Maintenance

## Routine checklist

- Pull the current `main` branch and review open dependency updates.
- Run `python scripts/project_status.py` and `make quality-gate`.
- Confirm workflow badges and all four documentation indexes.
- Review tracked results for accidental regeneration.
- Keep tests beside new behavior and update documentation in all four languages.

## After a new file

- Add essential files to `KEY_FILES` when appropriate.
- Link user-facing documents from every localized index.
- Add a test when a script or checker gains behavior.

## Before a demo or release

Use a clean branch, confirm Git status, inspect recent commits, review limitations, and verify that displayed results match the current code and release notes.

Do not remove historical tags or force-update published releases.
