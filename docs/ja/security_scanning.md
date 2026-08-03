🌐 言語: [English](../en/security_scanning.md) | [日本語](../ja/security_scanning.md) | [한국어](../ko/security_scanning.md) | [ไทย](../th/security_scanning.md)

# セキュリティスキャン

CodeQLは `main` へのプッシュ、`main` を対象とするプルリクエスト、週次スケジュールでPythonコードを解析します。

## ローカル準備

```bash
python -m pip check
make checks
make quality-gate
```

マージ前に依存関係の警告とCodeQLの検出結果を確認します。スキャンを通過しても、制御方策の安全性や安定性が証明されるわけではありません。ソフトウェアセキュリティと制御システムの安全性は、異なる観点からレビューする必要があります。

脆弱性の疑いは、リポジトリの[セキュリティ方針](../../SECURITY.ja.md)に従って非公開で報告してください。機密情報、個人データ、攻撃手法の詳細を公開Issueに記載しないでください。
