🌐 言語: [English](../en/presentation_outline.md) | [日本語](../ja/presentation_outline.md) | [한국어](../ko/presentation_outline.md) | [ไทย](../th/presentation_outline.md)

# プレゼンテーション構成

1. **動機:** Neural controllerは柔軟だが、安定性とrobustnessの評価が必要。
2. **Plant:** Position、velocity、force inputを持つmass-spring-damper state-space model。
3. **Baseline:** LQRが安定化referenceとimitation targetを提供。
4. **Neural controller:** Zero-at-origin architecture、imitation loss、Lyapunov penalty。
5. **評価:** Trajectory、settling time、cost、control effort、sampled `V_dot`。
6. **Robustness:** Actuator saturation、measurement noise、parameter variation。
7. **State-space evidence:** Phase portrait、Lyapunov contour、region-of-attraction map。
8. **主結果:** Test setting内でneural controllerはLQRに近く、追跡されたsampled Lyapunov violation fractionは全てzero。
9. **制約:** Simulated linear plant、finite grid、選択したuncertainty case、formal proofなし。
10. **今後:** Nonlinear system、formal verification、learned Lyapunov function、KAN、hardware validation。

数値主張を示すときは読めるcaption付きfigureを使い、seedとtested regionを明記します。
