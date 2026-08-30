🌐 言語: [English](../en/thesis_plan.md) | [日本語](../ja/thesis_plan.md) | [한국어](../ko/thesis_plan.md) | [ไทย](../th/thesis_plan.md)

# Thesis Plan

このドキュメントは、Lyapunov Neural-Network Control Lab を卒業研究計画に接続するための整理です。

## Tentative title

Lyapunov-style stability evaluation of neural-network controllers for a mass-spring-damper system

## Background

neural-network controllers は nonlinear control policies を近似できますが、その stability behavior の保証は難しい課題です。

LQR のような classical control methods は、linear systems に対して信頼できる baseline を提供します。

この project は、LQR teacher から学習した neural-network controller を Lyapunov-style checks で評価します。

## Research objective

目的は、neural-network controller が LQR を模倣しつつ、simulation において有用な closed-loop stability behavior を維持できるかを評価することです。

## Proposed method

1. mass-spring-damper system を定義する。
2. baseline として LQR controller を設計する。
3. LQR controller から training data を生成する。
4. neural-network controller を学習する。
5. stability-aware training penalty を追加する。
6. closed-loop responses をシミュレーションする。
7. performance、robustness、Lyapunov-style stability behavior を評価する。

## Evaluation items

- final normalized-state norm
- normalized settling time
- quadratic LQR-style cost
- integrated squared control effort
- maximum absolute normalized control input
- Lyapunov derivative behavior
- robustness under noise
- robustness under parameter variation
- actuator saturation behavior
- explicit sampling metadata を伴う finite-horizon convergence counts と fractions

## Expected contribution

期待される貢献は、performance metrics、robustness tests、Lyapunov-style stability checks を用いて古典 controller と neural-network controller を比較する、再現可能な Python research workflow です。

## Possible KAN extension

標準 neural-network controller が機能した後、同じ pipeline を KAN-based controller 比較へ拡張できます。

この比較では、同一設定下で KAN が imitation accuracy、smoothness、robustness、finite-horizon convergence を改善するかを検証できます。

## Risks and limitations

- 現在の plant は単純です。
- grid-based checks は global stability を証明しません。
- training region 外での neural-network behavior は信頼できない可能性があります。
- simulation results は hardware validation と同一ではありません。

## Possible final thesis structure

1. Introduction
2. LQR、neural-network control、Lyapunov stability の背景
3. System model と baseline controller
4. Neural-network controller design
5. Stability-aware training method
6. Simulation experiments
7. Robustness and finite-horizon convergence analysis
8. Discussion and limitations
9. Conclusion and future work
