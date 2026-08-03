🌐 言語: [English](../en/thesis_plan.md) | [日本語](../ja/thesis_plan.md) | [한국어](../ko/thesis_plan.md) | [ไทย](../th/thesis_plan.md)

# 卒業論文計画

## 仮題

機械力学系のためのLyapunovを意識したニューラルネットワーク制御

## 目的

LQR teacherから学習したneural controllerが、選択した非理想条件で有用なclosed-loop performance、sampled stability behavior、robustnessを維持できるか評価します。

## 手法

1. State-space plantとLQR baselineを導出。
2. Imitation lossとstability-aware lossでneural controllerを学習。
3. Trajectory、cost、effort、settling timeを比較。
4. Sampled Lyapunov behaviorと推定region of attractionを評価。
5. Saturation、noise、parameter variationを試験。
6. Limitationsとreproducibilityを文書化。

## 推奨章構成

1. 序論と関連研究
2. System modelとLQR設計
3. Neural controllerの学習
4. 安定性・robustness評価
5. 結果と考察
6. 制約、結論、今後の課題

現在のsystemはsimulation testbedです。Hardware validationとformal verificationは将来の拡張です。
