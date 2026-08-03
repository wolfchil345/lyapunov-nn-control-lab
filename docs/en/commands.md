🌐 Language: [English](../en/commands.md) | [日本語](../ja/commands.md) | [한국어](../ko/commands.md) | [ไทย](../th/commands.md)

# Command Guide

## Setup and diagnostics

```bash
python -m pip install -e .
python scripts/check_environment.py
```

## Run and verify

```bash
python examples/quick_start.py
python main.py
python -m pytest
make checks
make quality-gate
```

## Results

```bash
python scripts/list_results.py
python scripts/summarize_results.py
python scripts/new_experiment_log.py "short description"
```

`python scripts/clean_results.py` deletes every file in `results/`. Back up intended reference artifacts before running it.

## Git

```bash
git status -sb
git switch -c feature/short-description
git add <files>
git commit -m "Describe the change"
git push -u origin feature/short-description
```
