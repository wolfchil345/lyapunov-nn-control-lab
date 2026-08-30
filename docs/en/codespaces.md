🌐 Language: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# GitHub Codespaces Setup

This guide explains how to use the repository in GitHub Codespaces.

## Purpose

The repository includes `.devcontainer/devcontainer.json` so Codespaces can prepare a Python development environment automatically.

## What the dev container does

- Uses Python 3.11.
- Installs the package and its development dependencies from `pyproject.toml` after the Codespace is created.
- Recommends Python, Pylance, and GitHub Actions extensions.
- Enables pytest discovery from the `tests/` folder.

## First commands after opening Codespaces

```bash
python scripts/run_checks.py
```

## Run the experiment

```bash
python main.py
```

## Normal Git workflow

```bash
git switch main
git pull origin main
git switch -c feature/my-change
python scripts/run_checks.py
git status
```
