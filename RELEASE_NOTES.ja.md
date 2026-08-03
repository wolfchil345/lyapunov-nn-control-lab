🌐 言語: [English](RELEASE_NOTES.md) | [日本語](RELEASE_NOTES.ja.md) | [한국어](RELEASE_NOTES.ko.md) | [ไทย](RELEASE_NOTES.th.md)

# v1.0.1 - ドキュメントとリリースの改善

このpatch releaseはcore control experimentを変更せず、installation reliability、多言語documentation、result-summary reportingを改善します。

## ハイライト

- 不足していた `python-control` runtime dependencyを追加
- 生成virtual-environmentとpackage-metadata fileをignore
- 英語、日本語、韓国語、タイ語documentation foundationを追加
- 4言語のlocalized documentation indexを追加
- 各READMEをlocalized documentation indexへlink
- Obsoleteまたはnonexistent documentation linkを削除
- Ablation summaryが `lyapunov_violation_fraction` を読むよう修正
- 将来version tag向けにrelease checklistを一般化

## 検証

- 57 testがpass
- Quick-start exampleがpass
- Quality gateがpass
- Fixed random seedでexperiment resultの再生成に成功
- 再生成figureは以前の追跡figureとpixel-identical
- Lyapunov grid checkはzero violation
- Test controllerのregion-of-attraction checkは100% convergence

## 互換性

Core simulation、controller architecture、追跡experimental resultは `v1.0.0` から変更ありません。

---

# v1.0.0 - 最初の完全リリース

Lyapunov Neural-Network Control Labの最初のcomplete releaseです。

## ハイライト

- LQR baseline、imitation-trained neural controller、Lyapunov-inspired check
- Stability-aware penalty、saturation、noise、parameter robustness
- Phase portrait、Lyapunov contour、region-of-attraction analysis
- Stability-weight ablation、automatic report、model architecture diagram
- Methodology、project summary、citation metadata

## 主な出力

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png`
- `results/region_of_attraction_comparison.png`
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`

## 研究焦点

安定化古典controllerを模倣するneural controllerをLyapunov-based stability toolで評価できるか研究します。
