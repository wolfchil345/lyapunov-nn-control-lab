🌐 언어: [English](../en/methodology.md) | [日本語](../ja/methodology.md) | [한국어](../ko/methodology.md) | [ไทย](../th/methodology.md)

# 방법론

이 문서는 Lyapunov neural-network control lab에서 사용하는 주요 제어공학 개념을 설명합니다.

## 좌표 규약

이 저장소는 정규화된 무차원 2차 모델을 사용합니다. 정규화 시간은 `tau`, 정규화 위치 유사 좌표는 `q`, 정규화 속도는 `v = dq/dtau`, 정규화 제어 입력은 `u`, 상태는 `x = [q, v]`입니다. 따라서 `||x||_2 = sqrt(q^2 + v^2)` 및 `||x||_2^2 = q^2 + v^2`는 SI 위치/속도 측정치를 섞은 값이 아니라 정규화 상태 좌표의 Euclidean 크기입니다.

## 1. 질량-스프링-댐퍼 시스템

이 프로젝트는 2차 질량-스프링-댐퍼 시스템을 다룹니다.

```text
x = [q, v]
```

시스템은 다음 상태공간 형태로 작성됩니다.

```text
dx/dtau = A x + B u
```

여기서 x는 상태, u는 제어 입력, A는 플랜트 동역학, B는 입력이 플랜트에 미치는 영향을 나타냅니다.

공칭 파라미터에서 `A`의 고유값은 `-0.2 + 1.4j`와 `-0.2 - 1.4j`입니다. 두 고유값 모두 실수부가 음수이므로 무제어 공칭 선형 플랜트는 이미 점근 안정합니다. LQR은 과도응답과 제어 절충을 바꾸며, 이 프로젝트는 개루프 불안정 공칭 플랜트의 안정화가 아니라 모방, 성능, 강건성, 안정 거동 보존을 연구합니다.

## 2. LQR 기준 제어기

Linear Quadratic Regulator를 고전적 최적제어 기준으로 사용합니다.

```text
u = -Kx
```

`Q`와 `R`은 무차원 목적함수 가중치입니다. 결과 적분값은 물리 에너지가 아니라 quadratic LQR-style cost입니다. LQR은 신경망이 모방할 강력한 기준 제어기를 제공합니다.

## 3. 신경망 제어기

신경망 제어기는 정규화된 `q`와 `v`를 입력으로 받아 정규화 스칼라 제어 입력 하나를 출력합니다.

```text
NN(x) ≈ LQR(x)
```

이는 모방 학습이며, 신경망은 샘플 상태에서 LQR 제어기의 동작을 학습합니다.

## 4. Lyapunov 안정성 확인

Lyapunov 함수는 안정성을 추론하는 데 쓰는 에너지 유사 함수입니다.

```text
V(x) = x^T P x
```

폐루프 동역학을 따른 도함수는 다음과 같습니다.

```text
V-dot(x) = 2 x^T P (A x + B pi(x))
```

평가기는 서로 구분되는 두 가지 샘플 조건을 보고합니다.

```text
basic decrease: V-dot(x) <= 0
decay margin:   V-dot(x) + alpha * ||x||_2^2 <= 0
```

`alpha > 0`일 때 두 번째 조건이 더 강합니다. 정확한 평형점은 `V(0) = V-dot(0) = 0`이므로 제외되며 주변 이웃은 숨기지 않습니다. 기본 수치 허용오차 `1e-9`는 `alpha`와 분리되어 부동소수점 노이즈를 처리합니다. 격자 결과는 유한 샘플 영역만 다루며 연속 상태공간 안정성의 형식 인증이 아닙니다.

## 5. 안정성 인지 학습

신경망은 모방 손실과 Lyapunov 안정성 페널티를 함께 사용해 학습합니다.

```text
total loss = imitation loss + stability penalty
```

`alpha = 0.05`에서 학습은 평가와 동일한 감쇠 잔차의 양의 부분을 최소화합니다.

```text
decay residual = V-dot(x) + alpha * ||x||_2^2
stability penalty = mean(ReLU(decay residual))
```

## 6. 액추에이터 포화

프로젝트는 정규화 제어 입력 제한도 시험합니다.

```text
u = clip(u, -u_max, u_max)
```

이로써 액추에이터 제한이 폐루프 안정성과 성능에 미치는 영향을 보여줍니다。

## 7. 강건성 실험

프로젝트는 학습된 제어기가 불완전 조건에서 유효한지 평가합니다。

노이즈 강건성 실험은 측정 노이즈를 추가합니다。

```text
x_measured = x + noise
```

동일한 스칼라 Gaussian 표준편차를 정규화 좌표 `q`와 `v`에 독립적으로 적용합니다。

요청한 각 진폭은 동일한 반복 seed 목록으로 평가됩니다. 각 seed에 대해 시뮬레이션은 하나의 표준화 Gaussian 시퀀스를 생성하고 이를 각 진폭으로 스케일합니다(common random numbers). 이 설계는 seed-쌍 비교를 만들지만, 모든 확률/플랫폼 불확실성이 제거되었다는 뜻은 아닙니다。

stability-weight ablation도 같은 쌍원칙을 따릅니다. 모든 가중치가 동일한 명시적 model-initialization seeds를 사용합니다. seed별 trial 행은 집계 평균, 표본 표준편차, 표준오차와 분리해 유지합니다。

parameter robustness 실험은 정규화 질량, 감쇠, 강성 계수를 바꿔 모델링 오차를 모사합니다。

## 8. 위상 궤적과 Lyapunov 등고선

위상 궤적은 정규화 위치 대 정규화 속도를 그려 궤적이 원점으로 향하는지 보여줍니다。

Lyapunov 등고선 그림은 Lyapunov 함수 레벨셋 위에 궤적을 중첩합니다。

이 그림들은 폐루프 안정 거동을 시각적으로 설명합니다。

## 9. 유한 시간 수렴 분석

각 샘플 초기 상태 `x0`에 대해 실험은 `0 <= t <= T`에서 `x(t; x0)`를 시뮬레이션하고 아래의 엄격한 기준을 정확히 적용합니다。

```text
||x(T)||_2 < epsilon
```

평가기는 시뮬레이션이 성공적으로 `T`에 도달하고 시간/상태 값이 유한할 것을 요구합니다. 실패 또는 비유한 출력은 비수렴으로 조용히 분류하지 않고 오류를 발생시킵니다。

`T`는 정규화 시간이고 `epsilon`은 정규화 상태 Euclidean 허용오차입니다. 결과는 시간지평 `T`, 허용오차 `epsilon`, 격자 경계/해상도, 시험 수, 수렴 수, 수렴 비율을 기록합니다. 이는 샘플 유한 시간 수렴 맵입니다. 느리게 수렴하는 상태는 `t -> infinity`에서 수렴하더라도 `T`에서 실패할 수 있으므로, 실패가 곧 수학적 끌림영역 밖임을 뜻하지 않습니다。

원점 평형의 참 끌림영역은 개념적으로 다음과 같습니다。

```text
R = {x0 : x(t; x0) -> 0 as t -> infinity}.
```

유한 시뮬레이션은 이 정의를 검증하지 않습니다. 방어 가능한 추정에는 감소가 검증된 불변 Lyapunov 서브레벨셋, 적용 가능한 sum-of-squares 방법, 도달성/불변성 분석, 형식 검증, 또는 적합한 선형계의 해석 결과가 필요할 수 있습니다. `{x : V(x) <= c}`를 그렸다는 사실만으로 인증된 끌림영역이 되지 않습니다。

유한 시간 맵과 별도의 샘플 Lyapunov 점검은 서로 다른 질문에 답하며, 둘 다 연속 상태 끌림영역의 형식 인증이 아닙니다。

## 10. Stability-weight ablation study

ablation study는 서로 다른 Lyapunov penalty 가중치로 제어기를 학습합니다。

basic derivative violation fraction과 더 강한 decay-margin violation fraction을 분리 보고하고, final normalized-state norm, normalized settling time, quadratic LQR-style cost, integrated squared control effort를 함께 제시합니다. 마지막 항목은 `integral u^2 dtau`이며 물리 에너지가 아닙니다。

## 11. 요약

이 프로젝트는 고전 제어, 신경망 모방 학습, Lyapunov 분석, 강건성 시험, 샘플 유한 시간 수렴 분석을 결합합니다。

핵심 연구 질문은 다음과 같습니다。

```text
Can a neural-network controller imitate an LQR reference while preserving useful transient, robustness, and sampled Lyapunov behavior?
```
