🌐 言語: [English](../en/result_review_checklist.md) | [日本語](../ja/result_review_checklist.md) | [한국어](../ko/result_review_checklist.md) | [ไทย](../th/result_review_checklist.md)

# 結果レビュー用チェックリスト

## 設定

- [ ] Branch、commit、seed、epochs、model architectureを記録した。
- [ ] Initial condition、duration、grid density、noise、parameter caseを記録した。
- [ ] 比較runは意図した変数だけが異なる。

## 出力

- [ ] 期待するCSV、report、model、figureが存在する。
- [ ] Figureのlabelが読め、軌道が妥当である。
- [ ] Metricが有限で、複数を合わせて解釈している。
- [ ] Saturation、noise、parameter caseを明確に表示している。

## 安定性の主張

- [ ] サンプルLyapunov checkを経験的証拠と説明している。
- [ ] Region-of-attractionの主張にtest grid、horizon、thresholdを示している。
- [ ] Failure caseと予想外の挙動を残し、説明している。

## Commit前

- [ ] `make quality-gate` がpassする。
- [ ] `git diff` は意図したartifactだけを含む。
- [ ] Documentationとexperiment logが生成結果と一致する。
