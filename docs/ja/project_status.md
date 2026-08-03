🌐 言語: [English](../en/project_status.md) | [日本語](../ja/project_status.md) | [한국어](../ko/project_status.md) | [ไทย](../th/project_status.md)

# プロジェクトの状態

次を実行します。

```bash
python scripts/project_status.py
```

このコマンドは、重要なリポジトリファイルの有無を確認し、ドキュメント、スクリプト、テスト、ワークフロー、結果成果物の数を表示します。これはファイル構成の確認であり、テストや科学的レビューの代わりにはなりません。

## 使用するタイミング

- ファイル構成を変更した後。
- プルリクエスト、デモ、リリースの前。
- ドキュメント、スクリプト、テスト、ワークフローを追加した後。

新しいファイルが必須になった場合は、`scripts/project_status.py` の `KEY_FILES` を更新します。[品質ゲート](quality_gate.md)は、より広範な検証の一部としてこの状態確認を実行します。
