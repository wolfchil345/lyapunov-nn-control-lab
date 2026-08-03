🌐 언어: [English](../en/kan_extension.md) | [日本語](../ja/kan_extension.md) | [한국어](../ko/kan_extension.md) | [ไทย](../th/kan_extension.md)

# KAN 확장

## 질문

Kolmogorov-Arnold Network controller가 test region의 closed-loop stability와 robustness를 유지하면서 현재 MLP controller와 같거나 더 나을 수 있는가?

## 구현 계획

1. `src/controllers.py`에 같은 state-to-force interface의 KAN controller 추가.
2. Dataset, seed, training region, initial state, evaluation pipeline 고정.
3. Shape, `u(0) = 0`, serialization, simulation compatibility test 추가.
4. 같은 metric과 plot으로 LQR, MLP, KAN 비교.

## 평가

Imitation loss, settling time, quadratic cost, control energy, maximum input, sampled Lyapunov violation fraction, robustness, estimated region of attraction을 비교합니다.

## 주의

해석하기 쉬운 architecture가 자동으로 더 안정적인 controller인 것은 아닙니다. MLP와 같은 limitations, review process, formal-proof caveat를 적용합니다.
