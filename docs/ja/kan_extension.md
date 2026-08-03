🌐 言語: [English](../en/kan_extension.md) | [日本語](../ja/kan_extension.md) | [한국어](../ko/kan_extension.md) | [ไทย](../th/kan_extension.md)

# KANへの拡張

## 問い

Kolmogorov-Arnold Network controllerは、test region内のclosed-loop stabilityとrobustnessを保ちながら現在のMLP controllerと同等以上になれるか?

## 実装計画

1. `src/controllers.py` に同じstate-to-force interfaceを持つKAN controllerを追加。
2. Dataset、seed、training region、initial state、evaluation pipelineを固定。
3. Shape、`u(0) = 0`、serialization、simulation compatibilityのtestを追加。
4. 同一metricとplotでLQR、MLP、KANを比較。

## 評価

Imitation loss、settling time、quadratic cost、control energy、maximum input、sampled Lyapunov violation fraction、robustness、estimated region of attractionを比較します。

## 注意

より解釈しやすいarchitectureが自動的により安定なcontrollerになるわけではありません。MLPと同じlimitations、review process、formal-proof caveatを適用します。
