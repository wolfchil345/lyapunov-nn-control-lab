🌐 言語: [English](../en/results_interpretation.md) | [日本語](../ja/results_interpretation.md) | [한국어](../ko/results_interpretation.md) | [ไทย](../th/results_interpretation.md)

# Results Interpretation ガイド

このガイドは、Lyapunov Neural-Network Control Lab の主要出力をどのように解釈するかを説明します。

## Controller comparison

このプロジェクトは、古典的 LQR controller と、Lyapunov 安定性を考慮しながら LQR を模倣するよう学習された neural-network controller を比較します。

一般に、良い controller behavior は次を意味します。

- state が原点へ向かう
- final state norm が小さくなる
- settling time が妥当である
- control input が不必要に大きくない
- Lyapunov derivative がチェック領域で概ね負である

## Important metrics

以下の state magnitude はすべて、normalized・無次元座標における `||x||_2 = sqrt(q^2 + v^2)` を使用します。time と control input も同様に normalized です。

### `final_state_norm`
目標平衡点からの Euclidean normalized-state 距離を表します。小さいほど良いです。

### `settling_time`
canonical metric は `settling_time` です。`||x||_2 <= 0.02` の外側にある最後のサンプル以降、最初に観測される normalized time を取ります。つまり、それ以降の全サンプルは閉じた許容集合内に残ります。`settling_time_s` は historical compatibility alias であり seconds を意味しません。

### `quadratic_cost`
`x^T Q x + u^T R u` を normalized time 上で積分した値です。`Q` と `R` は無次元 objective weight なので、これは物理エネルギーではありません。

### `integrated_squared_control_effort`
`u^2` を normalized time 上で積分します。小さいほど controller は攻撃的でないことを示しますが、この値は物理エネルギーではありません。`control_energy` は historical compatibility alias として残されています。

### `max_abs_control`
normalized control input の絶対値最大を示します。saturation の確認に有用です。

## Sampled Lyapunov checks

このプロジェクトは二次関数とその閉ループ導関数を使用します。

```text
V(x) = x^T P x
V-dot(x) = 2 x^T P (A x + B pi(x))
```

2 つの metric は異なる問いに答えます。

- `derivative_violation_fraction` は、`V-dot` が numerical tolerance を超える sampled nonzero states の割合を数えます。
- `decay_margin_violation_fraction` は、`V-dot + alpha * ||x||_2^2` が numerical tolerance を超える sampled nonzero states の割合を数えます。

`alpha > 0` では 2 つ目の条件の方が強い条件です。学習と評価は同じ既定値 `alpha = 0.05` を使用します。既定 numerical tolerance は `1e-9` で、floating-point noise の処理のみに使われ、科学的 decay margin の一部として解釈してはいけません。

厳密な原点は `V(0) = V-dot(0) = 0` のため除外され、他の grid point はすべて含まれます。両 fraction は有限 sampled grid のみを記述し、連続状態空間での形式証明ではありません。

## Finite-horizon convergence map

有限 grid 上の各 initial state について、評価器は指定 horizon `T` までシミュレーションし、strict final-state criterion `||x(T)||_2 < epsilon` を満たす場合のみその state を分類します。`T` は normalized-time horizon、`epsilon` は normalized-state Euclidean tolerance です。報告された percentage は、`T`、`epsilon`、state bounds、grid resolution、tested/converged counts と合わせて解釈してください。

より大きい percentage は、その特定 finite-time criterion を満たした sampled state が多いことを意味します。これは asymptotic convergence、stable region、数学的 attraction basin を確立しません。収束が遅い state は、後で収束する場合でも `T` では失敗し得ます。

この map は上記 sampled Lyapunov checks とも別物です。どちらのテストも、形式的 continuous-state attraction-region certificate ではありません。

## Robustness experiments

### Measurement noise
noise robustness は、normalized `q` と `v` の measurement に同じ scalar Gaussian standard deviation を独立適用します。

今後の run は common random numbers を使い、各 noise amplitude を seed ごとにペア比較します。固定 seed では同じ standardized Gaussian sequence を各 amplitude へスケーリングして使います。raw の `noise_std x seed` 行を、aggregate mean、sample standard deviation、standard error より先に解釈してください。この pairing は random-realization confounding の一因を減らしますが、すべての不確かさを除去しません。

### Parameter variation
parameter robustness は、normalized mass、damping、stiffness 係数が変化したときにも controller が機能するかを確認します。

### Actuator saturation
saturation experiment は、normalized control input が制限されたときに controller が有効性を維持するかを確認します。

## Ablation study

stability-weight ablation は、報告する decay margin を明示したまま、学習時の Lyapunov penalty 乗数を変化させます。

今後の run は、すべての weight で同じ repeated seed set を使います。raw table は `stability_weight x seed` ごとに 1 行、aggregate table は weight ごとに `n`、mean、sample standard deviation、standard error を報告します。mean ± sample standard deviation は variability summary であり confidence interval ではありません。

有用な stability weight は、imitation accuracy、convergence、そして 2 種類の sampled Lyapunov metrics のバランスを取る必要があります。コミット済み `results/stability_weight_ablation.csv` は historical ambiguous violation column を使っており、ここでは意図的に上書きしません。再生成 schema も事後的に relabel しません。新しい paired files では、補正済みの sampled derivative / sampled decay-margin violation 名を使います。

## Practical reading order

1. `performance_metrics.csv` を確認する。
2. `position_comparison.png` を開く。
3. `phase_portrait.png` を開く。
4. `lyapunov_contours.png` を開く。
5. 新しい run 後は `finite_horizon_convergence_comparison.png` を開く。tracked `region_of_attraction_comparison.png` は historical pre-migration artifact です。
6. `experiment_report.md` を読む。
