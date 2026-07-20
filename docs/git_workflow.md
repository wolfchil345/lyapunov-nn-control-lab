# Git Workflow Guide

This guide explains the branch workflow used in this project.

## Basic rule

Do not work directly on `main`.

Create a feature branch, make one focused improvement, test it, then merge it into `main`.

## Standard branch flow

```bash
git switch main
git pull origin main
git switch -c feature/example-name
```

After editing files, run checks:

```bash
python scripts/check_environment.py
python scripts/project_status.py
python scripts/check_workflow_badges.py
python scripts/quality_gate.py
make checks
```

Commit and push:

```bash
git add path/to/changed_file.md
git commit -m "Describe the focused change"
git push -u origin feature/example-name
```

Merge into `main`:

```bash
git switch main
git pull origin main
git merge --no-ff feature/example-name
python scripts/quality_gate.py
make checks
git push origin main
```

Delete the feature branch:

```bash
git branch -d feature/example-name
git push origin --delete feature/example-name
```

## Branch naming style

Use short names that explain the purpose:

- `feature/add-new-guide`
- `feature/test-new-script`
- `feature/status-new-file`
- `feature/update-quality-gate`

## Commit message style

Use a clear action phrase:

- `Add maintenance guide`
- `Track maintenance guide in project status`
- `Add workflow badge checker tests`

## When Git says nothing to commit

If Git says there is nothing to commit, the change may already be committed.

Run:

```bash
git status
git log --oneline -5
```

If the correct commit exists, push the branch:

```bash
git push -u origin feature/example-name
```

## Portfolio note

This workflow shows that the project is maintained with careful version control, isolated changes, and repeatable checks.
