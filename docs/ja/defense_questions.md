🌐 言語: [English](../en/defense_questions.md) | [日本語](../ja/defense_questions.md) | [한국어](../ko/defense_questions.md) | [ไทย](../th/defense_questions.md)

# 発表・口頭試問の質問

## 動機と設計

**なぜLQRを使うか?** 透明性のある安定化baselineであり、線形公称plantに信頼できるimitation targetを与えるためです。

**Networkは何を学ぶか?** Positionとvelocityからscalar control forceへのmappingです。

**なぜ `u(0) = 0` を強制するか?** 目標で非zero commandがあると意図したequilibriumを壊す可能性があるためです。

## 安定性

**Grid checkはglobal stabilityを証明するか?** いいえ。一つのLyapunov candidateで有限個のsampled stateを評価します。

**なぜLyapunov penaltyを使うか?** Imitation errorだけではclosed-loop decayを直接測れません。Penaltyは学習中にsampled decay conditionを促します。

## 評価

**最重要metricは?** 単一では決められません。Convergence、cost、effort、sampled stability、robustnessを合わせて解釈します。

**なぜsaturation、noise、parameter variationを試すか?** 実制御器には入力制限、sensor誤差、model mismatchがあるためです。

## 制約と次の研究

Plantは単純で、証拠は全てsimulationであり、training region外の挙動は不確かです。Nonlinear plant、formal verification、hardware experiment、KANなどの別architectureが強化案です。
