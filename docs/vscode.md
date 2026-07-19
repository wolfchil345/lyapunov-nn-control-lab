# VS Code Setup

This guide explains how to use the project in VS Code or GitHub Codespaces.

## Recommended extensions

The repository includes `.vscode/extensions.json` with recommended extensions for Python development and GitHub Actions.

Recommended extensions:

- Python
- Pylance
- GitHub Actions

## Open the project

Open the repository root folder in VS Code. The root folder should contain `README.md`, `main.py`, `src/`, `tests/`, and `scripts/`.

## Select Python interpreter

After creating a virtual environment, select the interpreter from `.venv` in VS Code.

## Run checks from the terminal

```bash
python scripts/run_checks.py
```

## Run tests from VS Code

The repository includes `.vscode/settings.json` so VS Code can discover pytest tests from the `tests/` folder.

## Codespaces note

In Codespaces, open the terminal and run the same commands used locally:

```bash
pip install -r requirements.txt
python scripts/run_checks.py
```

## Common workflow

```bash
git switch main
git pull origin main
git switch -c feature/my-new-change
python scripts/run_checks.py
git status
```
