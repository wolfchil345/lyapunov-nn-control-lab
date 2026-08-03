🌐 言語: [English](../pull_request_template.md) | [日本語](pull_request_template.ja.md) | [한국어](pull_request_template.ko.md) | [ไทย](pull_request_template.th.md)

# Pull Request

## 概要

限定した変更と必要な理由を説明してください。

## 種類

- [ ] Bug fix
- [ ] Experimentまたはscientific change
- [ ] Documentationまたはtranslation
- [ ] Test、tooling、refactoring

## 科学的影響と生成ファイル

- 変更したseed、parameter、architecture、loss、metric:
- 変更したplot、CSV、report、model artifact:
- 想定する数値差とlimitations:

## 検証

- [ ] `git diff --check`
- [ ] `make checks`
- [ ] `make quality-gate`
- [ ] 必要なviewer-facing documentationを4言語で更新
- [ ] Generated artifactをreviewし意図してinclude

## Follow-up

未解決workを記載するか `None` と書いてください。
