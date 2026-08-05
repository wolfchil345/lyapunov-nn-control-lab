# Environment Setup

This guide explains how to prepare a local Python environment for the Lyapunov neural network control lab.

## Recommended Python version

Use Python 3.10 or newer.

## Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## Install the project

For normal use:

```bash
python -m pip install -e .
```

For development, tests, and package builds:

```bash
python -m pip install -e ".[dev]"
```

## Run local checks

```bash
python scripts/run_checks.py
```

This command runs documentation link checks, unit tests, and the quick start example.

## Run the main experiment

```bash
python main.py
```

## Common problems

- If imports fail, make sure you are running commands from the repository root.
- If runtime packages are missing, run `python -m pip install -e .` again.
- If test or build tools are missing, run `python -m pip install -e ".[dev]"`.
- If generated results look old, clean the results directory before rerunning experiments.

## Check the environment

Use the environment checker when Codespaces or a local machine has dependency problems:

```bash
python scripts/check_environment.py
```

This checks Python, required project files, the installed package, and all declared runtime imports.
