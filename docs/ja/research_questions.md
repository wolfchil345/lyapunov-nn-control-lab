🌐 言語: [English](../en/research_questions.md) | [日本語](../ja/research_questions.md) | [한국어](../ko/research_questions.md) | [ไทย](../th/research_questions.md)

# 研究課題

## 主な問い

ニューラル制御器は安定化LQR policyを模倣しながら、閉ループsimulationで良好なサンプルLyapunov挙動とrobustnessを維持できるか?

## 性能と安定性

- Settling time、quadratic cost、control effortはLQRにどの程度近いか?
- サンプル `V_dot` はどこで非負となり、training penaltyによりどう変わるか?
- 推定region of attractionはLQR、neural、saturated controllerでどう変わるか?

## ロバスト性

- Measurement noise、actuator saturation、plant uncertaintyは収束にどう影響するか?
- どのtest caseが最初に失敗し、それはtraining regionの内側か外側か?

## 学習とアーキテクチャ

- Imitation accuracyとstability-loss weightのtrade-offは何か?
- KAN controllerはsmoothness、interpretability、robustness、region-of-attraction resultを変えるか?

回答を報告するときはsampled region、threshold、seed、limitationsを明記します。
