🌐 言語: [English](../en/project_summary.md) | [日本語](../ja/project_summary.md) | [한국어](../ko/project_summary.md) | [ไทย](../th/project_summary.md)

# プロジェクト概要

## 目的

Lyapunov NN Control Labは、機械system、古典制御、neural network、安定性解析を結ぶ再現可能なresearch・portfolio projectです。

## アプローチ

Mass-spring-damper plantをmodel化し、LQR baselineを設計し、LQR state-feedback lawを模倣するneural controllerを学習します。Trainingにはsampled Lyapunov penaltyも含みます。複数initial state、quantitative metric、actuator saturation、measurement noise、plant-parameter variation、sampled Lyapunov behavior、estimated region of attractionで評価します。

## 証拠

- Automated test、quick-start example、CI、quality gate。
- 追跡figure、CSV metric、生成experiment report。
- Fixed random seedとdocumented reproduction workflow。
- Empirical sampled evidenceとformal proofの誠実な区別。

## 現在の結果

追跡test setting内でneural controllerはLQR baselineに近く、選択initial stateから収束し、sampled Lyapunov violationはzeroです。これらはdocumented model、region、threshold、uncertainty scenarioに限定されます。

## ポートフォリオ価値

System modeling、optimal control、PyTorch training、numerical simulation、scientific evaluation、software testing、GitHub workflow、release management、多言語technical communicationを示します。
