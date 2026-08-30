🌐 Language: [English](../en/commands.md) | [日本語](../ja/commands.md) | [한국어](../ko/commands.md) | [ไทย](../th/commands.md)

# Command Cheat Sheet

This page collects useful commands for running and maintaining the Lyapunov Neural-Network Control Lab.

## Setup

Install the project with development tools:

```bash
python -m pip install -e ".[dev]"
```

## Quick start

Run the small beginner-friendly example:

```bash
python examples/quick_start.py
```

## Run all local checks

Run tests and the quick-start example:

```bash
python scripts/run_checks.py
```

## Run tests only

```bash
python -m pytest
```

## Run the main experiment

```bash
python main.py
```

## Summarize generated results

```bash
python scripts/summarize_results.py
```

## Verify a provenance-aware run

```bash
python scripts/verify_run.py results/runs/<run_id>
```

## Clean incomplete staging directories

```bash
python scripts/clean_results.py
```

## Check current Git branch

```bash
git branch --show-current
git status
```

## Start a new feature branch

```bash
git switch main
git pull origin main
git switch -c feature/my-new-feature
```

## Commit and push a feature branch

```bash
git add .
git commit -m "Describe the change"
git push -u origin feature/my-new-feature
```

## Merge a feature branch into main

```bash
git switch main
git pull origin main
git merge --no-ff feature/my-new-feature
python scripts/run_checks.py
git push origin main
```

## Makefile shortcuts

The repository includes a `Makefile` with common command shortcuts:

```bash
make check-env
make checks
make test
make quickstart
make experiment
make clean
make summarize
make verify-run RUN_DIR=results/runs/<run_id>
```

## CI command

GitHub Actions uses `make checks` to run the same local checks used during development.
