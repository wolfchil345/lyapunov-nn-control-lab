🌐 言語: [English](../en/vscode.md) | [日本語](../ja/vscode.md) | [한국어](../ko/vscode.md) | [ไทย](../th/vscode.md)

# VS Code設定

## 推奨拡張機能

- Python
- Pylance
- GitHub Actions

リポジトリのフォルダを開き、`.venv` のPythonインタープリタを選択して、統合ターミナルでリポジトリのルートからコマンドを実行します。

## 通常のワークフロー

```bash
python scripts/check_environment.py
python -m pytest
python main.py
make quality-gate
```

Pytestのテスト検出先は `tests/` に設定されています。別のインタープリタが使われている場合は `.venv` を再選択し、ウィンドウを再読み込みします。
