🌐 言語: [English](../en/vscode.md) | [日本語](../ja/vscode.md) | [한국어](../ko/vscode.md) | [ไทย](../th/vscode.md)

# VS Code設定

## 推奨拡張機能

- Python
- Pylance
- GitHub Actions

リポジトリのフォルダを開き、`.venv` のinterpreterを選択し、統合terminalでリポジトリのルートからコマンドを実行します。

## 通常のワークフロー

```bash
python scripts/check_environment.py
python -m pytest
python main.py
make quality-gate
```

Pytest discoveryは `tests/` に設定されています。別のinterpreterが使われている場合は `.venv` を再選択し、windowをreloadします。
