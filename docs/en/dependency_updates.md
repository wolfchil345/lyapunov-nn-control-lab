🌐 Language: [English](../en/dependency_updates.md) | [日本語](../ja/dependency_updates.md) | [한국어](../ko/dependency_updates.md) | [ไทย](../th/dependency_updates.md)

# Dependency Updates Guide

This project uses Dependabot to help monitor dependency updates.

## What Dependabot checks

- Python packages from the root dependency files.
- GitHub Actions used in workflow files.

## Schedule

Dependabot checks for updates weekly.

## Review checklist

When Dependabot opens an update pull request:

1. Read the package or action being updated.
2. Run local checks.
3. Review the changed version carefully.
4. Merge only if tests pass.

```bash
python scripts/check_environment.py
make checks
```

## Safety note

For research code, dependency updates should be tested before being used for final experiment results.
