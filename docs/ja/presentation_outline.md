🌐 言語: [English](../en/presentation_outline.md) | [日本語](../ja/presentation_outline.md) | [한국어](../ko/presentation_outline.md) | [ไทย](../th/presentation_outline.md)

# Presentation Outline

この outline は、授業・lab meeting・interview で Lyapunov Neural-Network Control Lab を説明する際に使用できます。

## 1. Project motivation

- neural-network controllers は柔軟ですが、信頼性の判断が難しい場合があります。
- control engineering では stability、robustness、interpretability が必要です。
- この project は Lyapunov-style stability checks を伴う neural-network control を探究します。

## 2. System model

- plant は mass-spring-damper system です。
- state は normalized position `q` と normalized velocity `v` を含みます。
- control input は normalized scalar で、物理 force unit は定義しません。

## 3. Baseline controller

- LQR を古典的 control baseline として使用します。
- neural-network controller は LQR を模倣するよう学習されます。

## 4. Neural-network controller

- model は state を control input に写像します。
- training では imitation loss と stability-aware penalty を用います。
- 原点を target equilibrium として扱います。

## 5. Stability analysis

- stability behavior の確認に Lyapunov-style function を使用します。
- grid-based checks で Lyapunov derivative が負になる領域を推定します。
- finite-horizon convergence map は、指定した normalized-time horizon と normalized-state tolerance に対して `||x(T)||_2 < epsilon` を満たす sampled initial states を報告します。
- この map は数学的な region of attraction ではありません。

## 6. Robustness experiments

- actuator saturation は input limits を確認します。
- measurement-noise experiments は noisy state feedback を確認します。
- parameter-variation experiments は、変化した normalized mass、damping、stiffness coefficients を確認します。

## 7. Main outputs

- `performance_metrics.csv`
- `position_comparison.png`
- `phase_portrait.png`
- `lyapunov_contours.png`
- `finite_horizon_convergence_comparison.png`
- `experiment_report.md`

## 8. Key contribution

- この project は、simulation、neural-network control、Lyapunov-style checks、robustness tests、automatic reports、documentation を 1 つの再現可能 repository に統合しています。

## 9. Limitations

- 実際の plants と比較すると system は単純です。
- grid checks は empirical evidence を与えますが、完全な global stability proof ではありません。
- neural-network controller は training region 外で挙動が悪化する可能性があります。

## 10. Future work

- より多くの nonlinear systems を検証する。
- neural Lyapunov functions を直接学習する。
- より強い formal verification を追加する。
- より多くの controller types と比較する。
- workflow を KAN-based controllers へ適用する。
