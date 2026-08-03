🌐 言語: [English](../pull_request_template.md) | [日本語](pull_request_template.ja.md) | [한국어](pull_request_template.ko.md) | [ไทย](pull_request_template.th.md)

# プルリクエスト

## 概要

限定した変更と必要な理由を説明してください。

## 種類

- [ ] バグ修正
- [ ] 実験または科学的変更
- [ ] ドキュメントまたは翻訳
- [ ] テスト、開発ツール、リファクタリング

## 科学的影響と生成ファイル

- 変更したシード、パラメータ、構成、損失、指標:
- 変更した図、CSV、レポート、モデル成果物:
- 想定する数値差と制約:

## 検証

- [ ] `git diff --check`
- [ ] `make checks`
- [ ] `make quality-gate`
- [ ] 必要なユーザー向けドキュメントを4言語で更新
- [ ] 生成された成果物をレビューし、意図したファイルのみを追加

## 今後の対応

未解決の作業を記載するか `None` と書いてください。
