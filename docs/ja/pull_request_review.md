🌐 言語: [English](../en/pull_request_review.md) | [日本語](../ja/pull_request_review.md) | [한국어](../ko/pull_request_review.md) | [ไทย](../th/pull_request_review.md)

# Pull Requestレビュー

## 一般レビュー

- [ ] Titleとsummaryが一つの限定された変更を説明する。
- [ ] Testとrequired checkがpassする。
- [ ] User-facing behavior変更時にdocumentを4言語で更新する。
- [ ] Generated fileを意図してincludeまたはignoreする。
- [ ] Merge前にconversationを解決する。

## 科学的レビュー

- [ ] Seed、plant parameter、controller architecture、loss、evaluation settingの変更が明示される。
- [ ] 数値とfigureのdiffを説明する。
- [ ] Sampled checkをformal proofとして示さない。
- [ ] Failure caseとlimitationsを残す。

## Local commands

```bash
git diff --check
make checks
make quality-gate
```

Latest commitが全required checkにpassした後、protected `main` branch経由でのみmergeします。
