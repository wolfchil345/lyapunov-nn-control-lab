🌐 言語: [English](../en/branch_protection.md) | [日本語](../ja/branch_protection.md) | [한국어](../ko/branch_protection.md) | [ไทย](../th/branch_protection.md)

# ブランチ保護ガイド

このガイドでは、リポジトリに推奨されるブランチ保護設定を説明します。

## 目的

`main` を保護し、重要な研究コードがマージされる前にレビューと確認を受けるようにします。

## 推奨設定

- マージ前に pull request を必須にする。
- マージ前に status check の成功を必須にする。
- マージ前にブランチが最新であることを必須にする。
- 最終学位論文やポートフォリオ用途では administrator も含める。
- `main` への force push を制限する。
- `main` のブランチ削除を制限する。

## 推奨される必須チェック

- ローカルチェック
- CodeQL

## マージ前のローカルチェックリスト

```bash
python scripts/check_environment.py
make checks
git status
```

## 推奨ワークフロー

変更ごとに feature ブランチを作成し、ローカルでチェックを実行し、GitHub のチェックが通ってからのみマージします。

## 注意

この文書はあくまで推奨事項です。実際のブランチ保護は GitHub リポジトリ設定で構成する必要があります。
