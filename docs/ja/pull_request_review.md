🌐 言語: [English](../en/pull_request_review.md) | [日本語](../ja/pull_request_review.md) | [한국어](../ko/pull_request_review.md) | [ไทย](../th/pull_request_review.md)

# Pull Requestのレビュー

## 一般レビュー

- [ ] Titleと概要が一つの限定された変更を説明する。
- [ ] テストと必須チェックが合格する。
- [ ] ユーザーから見える動作が変わる場合は、ドキュメントを4言語すべてで更新する。
- [ ] 生成ファイルを追跡するか無視するかを意図的に決める。
- [ ] Merge前にconversationを解決する。

## 科学的レビュー

- [ ] 乱数シード、プラントパラメータ、制御器構成、損失関数、評価設定の変更が明記されている。
- [ ] 数値と図の差分を説明する。
- [ ] サンプル点での 確認を形式的証明として示さない。
- [ ] 失敗 ケースと制約を残す。

## ローカルで実行するコマンド

```bash
git diff --check
make checks
make quality-gate
```

最新のコミットが必須チェックをすべて通過した後、保護された `main` ブランチ経由でのみマージします。
