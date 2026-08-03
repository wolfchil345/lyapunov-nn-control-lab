🌐 Language: [English](../en/environment.md) | [日本語](../ja/environment.md) | [한국어](../ko/environment.md) | [ไทย](../th/environment.md)

# Environment Setup

## Requirements

- Python 3.10 or newer; CI uses Python 3.11 and 3.12.
- Git and, for tracked binary assets, Git LFS.
- CPU execution is sufficient for the included experiments.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

## Verify the environment

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

Run commands from the repository root. If imports fail, reactivate `.venv` and reinstall with `python -m pip install -e .`.
