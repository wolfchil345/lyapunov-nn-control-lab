🌐 Language: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# Dependency Troubleshooting

Start with:

```bash
python scripts/check_environment.py
python -m pip check
```

## Missing package or PyTorch import error

Activate `.venv`, upgrade pip, and reinstall the project with `python -m pip install -e .`. Avoid mixing system Python and virtual-environment packages.

## Git LFS error

Install Git LFS, run `git lfs install`, and use `git lfs pull` to restore tracked binary assets.

## Clean reset

Create a new virtual environment instead of modifying the system interpreter. In Codespaces, rebuild the dev container if the environment remains inconsistent.

When asking for help, include the output of `python scripts/check_environment.py`, `python --version`, and `python -m pip check`.
