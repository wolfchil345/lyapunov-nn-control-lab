🌐 言語: [English](../en/limitations.md) | [日本語](../ja/limitations.md) | [한국어](../ko/limitations.md) | [ไทย](../th/limitations.md)

# 制約

## モデルとデータ

- Plantはsimulated linear mass-spring-damper systemです。
- Training stateはbounded regionを対象としLQR teacherを使います。
- Nonlinear plantやunseen stateへのgeneralizationを示しません。

## 安定性の証拠

- Quadratic Lyapunov functionは公称LQR設計から得ています。
- `V_dot` とregion-of-attraction評価はfinite grid、threshold、simulation horizonを使用します。
- Zero sampled violationはformalまたはglobal proofではありません。

## ロバスト性の証拠

- Actuator limit、noise level、parameter variationは選択scenarioであり、網羅的uncertainty setではありません。
- Numerical solverとdependency versionにより小さな差が生じます。
- Hardware、delay、quantization、fault、adversarial testを含みません。

## 責任ある利用

このrepositoryは教育研究softwareであり、安全認証済みcontrollerではありません。物理equipmentへ適用する前に独立検証してください。

今後はnonlinear plant、formal verification、learned Lyapunov function、広いuncertainty analysis、hardware validationを検討します。
