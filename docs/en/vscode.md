🌐 Language: [English](../en/vscode.md) | [日本語](../ja/vscode.md) | [한국어](../ko/vscode.md) | [ไทย](../th/vscode.md)

# VS Code Setup

## Recommended extensions

- Python
- Pylance
- GitHub Actions

Open the repository folder, select the interpreter from `.venv`, and run commands in the integrated terminal from the repository root.

## Normal workflow

```bash
python scripts/check_environment.py
python -m pytest
python main.py
make quality-gate
```

Pytest discovery is configured for `tests/`. If VS Code uses another interpreter, select `.venv` again and reload the window.
