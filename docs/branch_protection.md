# Branch Protection Guide

This guide explains recommended branch protection settings for the repository.

## Goal

Protect `main` so important research code is reviewed and checked before changes are merged.

## Recommended settings

- Require a pull request before merging.
- Require status checks to pass before merging.
- Require branches to be up to date before merging.
- Include administrators if this is used for final thesis or portfolio work.
- Restrict force pushes to `main`.
- Restrict branch deletion for `main`.

## Recommended required checks

- Local checks
- CodeQL

## Local checklist before merging

```bash
python scripts/check_environment.py
make checks
git status
```

## Suggested workflow

Create feature branches for each change, run checks locally, then merge only after GitHub checks pass.

## Note

This document is only a recommendation. Actual branch protection must be configured in the GitHub repository settings.
