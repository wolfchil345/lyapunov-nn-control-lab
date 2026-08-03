🌐 言語: [English](../en/faq.md) | [日本語](../ja/faq.md) | [한국어](../ko/faq.md) | [ไทย](../th/faq.md)

# よくある質問

## このprojectは何をするか?

Mass-spring-damper systemでLQRを模倣するneural controllerを学習し、performance、sampled Lyapunov behavior、robustnessを評価します。

## なぜLQRをteacherにするか?

LQRは透明で再現可能であり、公称linear plantを安定化するため、有用なbaselineとlabel sourceになります。

## 安定性を証明するか?

いいえ。二次Lyapunov candidateを使ったsimulationとfinite-grid evidenceを提供します。Formal continuous-domain verificationは現在の範囲外です。

## 通常のmachine-learning demoと何が違うか?

Closed-loop trajectory、control effort、cost、saturation、noise、model variation、Lyapunov behavior、estimated region of attractionを再現可能なsoftware checkと共に評価します。

## どう検証するか?

`python examples/quick_start.py`、`make checks`、`make quality-gate` を実行します。完全な実験は `python main.py` です。

## 最初に何を読むか?

[プロジェクト概要](project_summary.md)、[研究手法](methodology.md)、[実験ワークフロー](experiment_workflow.md)、[制約](limitations.md)を読みます。
