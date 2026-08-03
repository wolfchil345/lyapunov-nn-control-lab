🌐 言語: [English](ROADMAP.md) | [日本語](ROADMAP.ja.md) | [한국어](ROADMAP.ko.md) | [ไทย](ROADMAP.th.md)

# ロードマップ

## 短期

- 複数seedでneural trainingを繰り返し、分布またはconfidence intervalを報告。
- 実験選択CLIを追加し、高cost sweepを目的別commandに分割。
- 生成reportにdependency versionとexperiment configurationを記録。

## 制御とロバスト性

- 互換settingでPID、LQR、MPC、MLP、KAN controllerを比較。
- Nonlinear plant、external disturbance、delay、quantization、広いuncertainty setを追加。
- Region-of-attraction解析を拡張しfailure-case mapを保存。

## 安定性解析

- Alternativeおよびlearned Lyapunov functionを試験。
- Candidate violation付近にadaptive samplingを追加。
- Empirical grid checkとformal neural-network verification toolを比較。

## 物理検証

- 実機運用前にhardware-in-the-loop stageを構築。
- Actuator、sensor、safety constraintを明示。
- Safety-certified componentとresearch prototypeを分離。

## コミュニケーション

- Feature変更時も4言語documentationを完全に維持。
- 同じreproducible resultに基づくposterと短いtechnical articleを追加。

長期目標は信頼できるlearning-based control実験platformであり、一つのneural controllerがcontrol safety全般を解決するという主張ではありません。
