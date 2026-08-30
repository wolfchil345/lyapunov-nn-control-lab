🌐 언어: [English](../en/results_interpretation.md) | [日本語](../ja/results_interpretation.md) | [한국어](../ko/results_interpretation.md) | [ไทย](../th/results_interpretation.md)

# Results Interpretation 가이드

이 가이드는 Lyapunov Neural-Network Control Lab의 주요 출력 결과를 해석하는 방법을 설명합니다.

## Controller comparison

프로젝트는 고전적 LQR controller와, Lyapunov 안정성을 고려하면서 LQR을 모방하도록 학습된 neural-network controller를 비교합니다.

좋은 controller behavior는 보통 다음을 의미합니다.

- state가 원점으로 이동한다
- final state norm이 작아진다
- settling time이 합리적이다
- control input이 불필요하게 크지 않다
- Lyapunov derivative가 점검 영역에서 대체로 음수이다

## Important metrics

아래 state magnitudes는 모두 normalized, dimensionless 좌표의 `||x||_2 = sqrt(q^2 + v^2)`를 사용합니다. time과 control input도 normalized입니다.

### `final_state_norm`
목표 평형점으로부터의 Euclidean normalized-state 거리를 측정합니다. 작을수록 좋습니다.

### `settling_time`
canonical metric은 `settling_time`입니다. `||x||_2 <= 0.02` 바깥에 있었던 마지막 샘플 이후의 첫 normalized sampled time을 뜻합니다. 따라서 그 이후 샘플은 모두 닫힌 허용 집합 안에 남습니다. `settling_time_s`는 historical compatibility alias이며 seconds를 의미하지 않습니다.

### `quadratic_cost`
`x^T Q x + u^T R u`를 normalized time에서 적분합니다. `Q`와 `R`은 dimensionless objective weights이므로, 이는 물리 에너지가 아닙니다.

### `integrated_squared_control_effort`
`u^2`를 normalized time에서 적분합니다. 작을수록 제어기가 덜 공격적이라는 뜻이지만, 이 값은 물리 에너지가 아닙니다. `control_energy`는 historical compatibility alias로 유지됩니다.

### `max_abs_control`
정규화 control input의 절대값 최대치를 보여줍니다. saturation 점검에 유용합니다.

## Sampled Lyapunov checks

프로젝트는 다음의 이차 함수와 폐루프 도함수를 사용합니다.

```text
V(x) = x^T P x
V-dot(x) = 2 x^T P (A x + B pi(x))
```

두 metric은 서로 다른 질문에 답합니다.

- `derivative_violation_fraction`은 `V-dot`이 numerical tolerance를 초과하는 sampled nonzero states를 셉니다.
- `decay_margin_violation_fraction`은 `V-dot + alpha * ||x||_2^2`가 numerical tolerance를 초과하는 sampled nonzero states를 셉니다.

`alpha > 0`일 때 두 번째 조건이 더 강합니다. 학습과 평가는 동일한 기본값 `alpha = 0.05`를 사용합니다. 기본 numerical tolerance는 `1e-9`이며 floating-point noise 처리용일 뿐, 과학적 decay margin의 일부로 해석하면 안 됩니다.

정확한 원점은 `V(0) = V-dot(0) = 0`이므로 제외되고, 그 외 모든 grid point는 포함됩니다. 두 fraction 모두 유한 sampled grid만 설명하며, 연속 상태공간에 대한 형식적 인증이 아닙니다.

## Finite-horizon convergence map

유한 grid의 각 initial state에 대해, evaluator는 지정된 horizon `T`까지 시뮬레이션한 뒤 strict final-state criterion `||x(T)||_2 < epsilon`이 성립할 때만 해당 state를 분류합니다. `T`는 normalized-time horizon이고 `epsilon`은 normalized-state Euclidean tolerance입니다. 보고된 비율은 `T`, `epsilon`, state bounds, grid resolution, tested/converged counts와 함께 해석해야 합니다.

더 큰 비율은 그 특정 finite-time criterion을 만족한 sampled state가 더 많다는 뜻입니다. 이것이 asymptotic convergence, 안정 영역, 수학적 attraction basin을 확립하는 것은 아닙니다. 느리게 수렴하는 state는 나중에 수렴하더라도 `T`에서는 실패할 수 있습니다.

이 map은 위 sampled Lyapunov checks와도 다른 개념입니다. 두 테스트 모두 formal continuous-state attraction-region certificate가 아닙니다.

## Robustness experiments

### Measurement noise
noise robustness는 normalized `q` 및 `v` measurement에 동일한 scalar Gaussian standard deviation을 독립적으로 적용합니다.

향후 runs는 common random numbers를 사용해 각 noise amplitude를 seed별로 짝지어 비교합니다. 고정 seed에서는 같은 standardized Gaussian sequence를 각 amplitude로 스케일합니다. aggregate mean, sample standard deviation, standard error보다 raw `noise_std x seed` 행을 먼저 해석해야 합니다. 이 pairing은 random-realization confounding 한 원인을 줄이지만, 모든 불확실성을 제거하지는 않습니다.

### Parameter variation
parameter robustness는 normalized mass, damping, stiffness 계수가 바뀌어도 controller가 작동하는지 점검합니다.

### Actuator saturation
saturation experiment는 normalized control input이 제한될 때 controller가 효과를 유지하는지 점검합니다.

## Ablation study

stability-weight ablation은 보고되는 decay margin을 명시적으로 유지한 채 학습 중 Lyapunov penalty의 multiplier를 바꿉니다.

향후 runs는 모든 weight에 동일한 repeated seed set을 사용합니다. raw table은 `stability_weight x seed`당 1행이고, aggregate table은 weight별 `n`, mean, sample standard deviation, standard error를 보고합니다. mean ± sample standard deviation은 variability summary이지 confidence interval이 아닙니다.

유용한 stability weight는 imitation accuracy, convergence, 그리고 두 sampled Lyapunov metrics를 균형 있게 맞춰야 합니다. 커밋된 `results/stability_weight_ablation.csv`는 historical ambiguous violation column을 사용하며 여기서 의도적으로 덮어쓰지 않습니다. 재생성 schema도 사후 relabel하지 않습니다. 새 paired files는 수정된 sampled derivative 및 sampled decay-margin violation 이름을 사용합니다.

## Practical reading order

1. `performance_metrics.csv`를 확인한다.
2. `position_comparison.png`를 연다.
3. `phase_portrait.png`를 연다.
4. `lyapunov_contours.png`를 연다.
5. 새 run 후 `finite_horizon_convergence_comparison.png`를 연다. tracked `region_of_attraction_comparison.png`는 historical pre-migration artifact이다.
6. `experiment_report.md`를 읽는다.
