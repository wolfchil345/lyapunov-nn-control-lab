🌐 言語: [English](../en/pull_request_review.md) | [日本語](../ja/pull_request_review.md) | [한국어](../ko/pull_request_review.md) | [ไทย](../th/pull_request_review.md)

# Pull Request Review ガイド

このガイドは、変更を `main` にマージする前にどのようにレビューするかを説明します。

## レビューの目的

- 変更の目的が明確であることを確認する。
- ローカルチェックが通ることを確認する。
- 振る舞いが変わる場合はドキュメントが更新されていることを確認する。
- 実験結果が誤って上書きされていないことを確認する。
- 生成ファイルが意図して含まれているか、または無視されていることを確認する。

## マージ前のローカルコマンド

```bash
python scripts/check_environment.py
make checks
git status
```

## レビュー用チェックリスト

pull request または feature branch をマージする前に、次を確認します。

- branch 名が変更内容を表していること。
- commit message が明確であること。
- テストがローカルで通ること。
- GitHub Actions が通ること。
- 必要であれば README または docs が更新されていること。
- result files は、有用な例または最終成果物である場合にのみ commit されていること。

## 研究向けのレビュー項目

- 変更は numerical results に影響するか。
- 変更は Lyapunov analysis に影響するか。
- 変更は reproducibility に影響するか。
- 変更は random seeds、model architecture、experiment settings を変えるか。

## マージ規則

チェックが通り、working tree が clean な場合にのみマージします。
