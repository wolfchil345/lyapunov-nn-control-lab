🌐 言語: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CIワークフロー

| ワークフロー | 目的 |
|---|---|
| `tests.yml` | Python 3.10と3.12でPythonテストスイートを実行 |
| `local-checks.yml` | Python 3.12でパッケージ、文書、lint、テスト、クイックスタートを確認 |
| `quality-gate.yml` | `main` とプルリクエストで完全な準備状況チェックを実行 |
| `codeql.yml` | プッシュ、プルリクエスト、週次スケジュールでPythonコードを解析 |

## プッシュ前

```bash
make checks
make quality-gate
```

ワークフローは読み取り専用の既定権限、依存関係キャッシュ、同時実行のキャンセル、明示的なタイムアウトを使用します。必須のブランチチェックには、GitHubに表示されるジョブ名を正確に使います。失敗した場合は、最初に失敗した手順を確認し、そのコマンドをローカルで再現します。

READMEのバッジは `python scripts/check_workflow_badges.py` で検証します。
