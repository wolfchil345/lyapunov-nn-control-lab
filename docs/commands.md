# Command Cheat Sheet

This page collects useful commands for running and maintaining the Lyapunov Neural-Network Control Lab.

## Setup

Install required packages:

```bash
pip install -r requirements.txt
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

## Clean generated results

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
```
