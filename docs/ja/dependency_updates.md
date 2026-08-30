🌐 言語: [English](../en/dependency_updates.md) | [日本語](../ja/dependency_updates.md) | [한국어](../ko/dependency_updates.md) | [ไทย](../th/dependency_updates.md)

# Dependency Updates ガイド

このプロジェクトでは Dependabot を使って依存関係の更新を監視します。

## Dependabot が確認する内容

- root の依存関係ファイルにある Python パッケージ。
- workflow ファイルで使われている GitHub Actions。

## スケジュール

Dependabot は毎週更新を確認します。

## レビュー用チェックリスト

Dependabot が更新 pull request を開いたら:

1. 更新される package または action を読みます。
2. ローカルチェックを実行します。
3. 変更された version を慎重に確認します。
4. テストが通った場合のみ merge します。

```bash
python scripts/check_environment.py
make checks
```

## 安全上の注意

研究コードでは、依存関係の更新は最終的な実験結果に使う前に必ずテストしてください。
