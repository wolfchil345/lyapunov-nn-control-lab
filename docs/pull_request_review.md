# Pull Request Review Guide

This guide explains how to review changes before merging them into `main`.

## Review goals

- Confirm the change has a clear purpose.
- Confirm local checks pass.
- Confirm documentation is updated when behavior changes.
- Confirm experiment results are not accidentally overwritten.
- Confirm generated files are intentionally included or ignored.

## Local commands before merge

```bash
python scripts/check_environment.py
make checks
git status
```

## Review checklist

Before merging a pull request or feature branch, check:

- The branch name describes the change.
- The commit message is clear.
- Tests pass locally.
- GitHub Actions pass.
- README or docs are updated if needed.
- Result files are only committed when they are useful examples or final artifacts.

## Research-specific review points

- Does the change affect numerical results?
- Does the change affect Lyapunov analysis?
- Does the change affect reproducibility?
- Does the change change random seeds, model architecture, or experiment settings?

## Merge rule

Merge only after checks pass and the working tree is clean.
