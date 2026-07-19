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

## Install dependencies

```bash
pip install -r requirements.txt
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
- If packages are missing, run `pip install -r requirements.txt` again.
- If generated results look old, clean the results directory before rerunning experiments.

## Check the environment

Use the environment checker when Codespaces or a local machine has dependency problems:

```bash
python scripts/check_environment.py
```

This checks Python, Git, Git LFS, required project files, and PyTorch import status.
