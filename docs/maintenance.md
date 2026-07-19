# Maintenance Guide

This guide explains how to keep the project healthy after new features, docs, tests, and workflows are added.

## Routine maintenance checklist

Run this checklist before merging into `main`:

```bash
python scripts/check_environment.py
python scripts/project_status.py
python scripts/check_workflow_badges.py
python scripts/quality_gate.py
make checks
```

## Weekly project check

Run:

```bash
git switch main
git pull origin main
python scripts/quality_gate.py
```

Then check:

- GitHub Actions are passing.
- README badges are visible.
- Important docs are linked from `docs/index.md`.
- New scripts have tests when possible.
- New important files are tracked by `scripts/project_status.py`.

## After adding a new script

1. Add the script under `scripts/`.
2. Add a test under `tests/` if the script has logic.
3. Add a Makefile shortcut if the command will be used often.
4. Add documentation if users need to understand it.
5. Add the script to `scripts/project_status.py` if it becomes part of the core project structure.

## After adding a new document

1. Place the file under `docs/`.
2. Link it from `docs/index.md`.
3. Link it from `README.md` if it is important for visitors.
4. Add it to `scripts/project_status.py` if it is a core guide.

## After adding or changing a workflow

1. Run the quality gate locally.
2. Confirm the workflow file is under `.github/workflows/`.
3. Add or update README badges if needed.
4. Run `python scripts/check_workflow_badges.py`.
5. Push and confirm GitHub Actions pass.

## Before a demo or professor meeting

Run:

```bash
python scripts/quality_gate.py
python scripts/project_status.py
```

Also open the README and confirm that the project goal, badges, docs, and quick-start instructions are easy to see.

## Portfolio note

A maintained repository is stronger than a one-time experiment. This checklist helps show that the project is stable, documented, and ready for review.
