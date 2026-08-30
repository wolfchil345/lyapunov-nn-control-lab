🌐 言語: [English](../en/defense_questions.md) | [日本語](../ja/defense_questions.md) | [한국어](../ko/defense_questions.md) | [ไทย](../th/defense_questions.md)

# Defense Questions

このドキュメントは、Lyapunov Neural-Network Control Lab を発表・ディフェンスする際に想定される質問と回答ポイントをまとめたものです。

## Project motivation

### Why use a neural-network controller?
- neural network は柔軟な control policy を近似できます。
- 非線形 systems では古典的 controller design が難しくなる場合があり、そのとき有用です。
- この project では、まず単純な system で検討しています。

### Why compare with LQR?
- LQR は線形 systems に対する信頼性の高い古典的 baseline です。
- imitation learning の teacher controller として明確です。
- LQR と比較することで neural controller を評価しやすくなります。

## Stability

### Why use Lyapunov-style checks?
- stability は control engineering において重要です。
- Lyapunov analysis は、system の energy-like behavior が減少するかを考察する枠組みを与えます。
- この project では grid-based checks を empirical な stability evidence として用います。

### Does this prove global stability?
- いいえ。
- grid check は sampled states のみを評価します。
- 解析を支援するものですが、完全な数学的証明ではありません。

## Experiments

### Why use a mass-spring-damper system?
- 単純で理解しやすく、control education で一般的です。
- position と velocity の state を持つため可視化しやすいです。
- より難しい nonlinear systems へ進む前の第一段階 testbed として適しています。

### Why test robustness?
- 実システムには noise、actuator limits、parameter uncertainty があります。
- robustness experiments は、選択した不完全条件でも controller が機能するかを示します。

## Neural-network training

### What does the neural network learn?
- state から control input への mapping を学習します。
- target control input は LQR controller から生成されます。

### Why add a stability-aware penalty?
- 純粋な imitation では LQR 出力に一致しても、closed-loop simulation で挙動が悪化する可能性があります。
- penalty は sampled states 周辺でより良い Lyapunov-style behavior を促します。

## Results interpretation

### Which metric is most important?
- 単一の metric だけでは不十分です。
- final normalized-state norm、normalized settling time、LQR-style cost、integrated squared control effort、Lyapunov behavior、robustness を合わせて解釈すべきです。

### What result would be considered successful?
- neural controller が原点近傍へ収束すること。
- LQR に近い性能を示すこと。
- チェック領域で Lyapunov derivative が概ね負であること。
- noise、saturation、parameter variation 下でも挙動が妥当であること。

## Limitations

### What are the main limitations?
- plant が単純です。
- simulation は hardware experiments ではありません。
- grid-based stability checks は empirical です。
- neural network は training region 外で失敗する可能性があります。

## Future work

### How can this become stronger research?
- nonlinear plants を検証する。
- formal verification を追加する。
- KAN-based controllers と比較する。
- neural Lyapunov functions を直接学習する。
- より現実的な control problems へ適用する。
