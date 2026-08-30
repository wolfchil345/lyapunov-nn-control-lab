🌐 언어: [English](../en/kan_extension.md) | [日本語](../ja/kan_extension.md) | [한국어](../ko/kan_extension.md) | [ไทย](../th/kan_extension.md)

# KAN Extension 가이드

이 가이드는 현재 Lyapunov Neural-Network Control Lab을 Kolmogorov-Arnold Network 제어기 실험 방향으로 확장하는 방법을 설명합니다.

## Motivation

현재 프로젝트는 표준 neural-network 제어기로 LQR을 모방하고 안정성 관련 거동을 평가합니다.

KAN-based 제어기는 시스템 상태를 제어 입력으로 매핑하는 대안 function approximator로 시험할 수 있습니다.

## Current controller pipeline

현재 워크플로는 다음과 같습니다.

1. mass-spring-damper system 정의
2. LQR 제어기에서 학습 데이터 생성
3. neural-network 제어기 학습
4. 폐루프 거동 시뮬레이션
5. performance metrics 계산
6. Lyapunov-style stability behavior 점검
7. robustness 및 finite-horizon convergence 실험 실행

## KAN controller idea

KAN 제어기는 표준 neural-network 모델을 KAN-style 모델로 교체하는 방식입니다.

입력은 여전히 시스템 상태입니다.

- position
- velocity

출력도 여전히 제어 입력입니다.

- normalized scalar control input

## Files that may need changes

### `src/controllers.py`
KAN controller class 또는 wrapper function 추가

### `main.py`
LQR 및 현재 neural-network controller와 함께 KAN 학습, 시뮬레이션, metrics, plotting 추가

### `src/plotting.py`
LQR, standard neural network, KAN 비교 plots 추가

### `tests/`
KAN controller가 유효한 scalar control을 반환하고 simulation에서 실행 가능한지 검증하는 tests 추가

## Suggested experiment design

세 가지 제어기를 비교합니다.

- LQR baseline
- standard neural-network controller
- KAN controller

모든 제어기에 동일한 초기 상태, metrics, Lyapunov checks를 사용합니다.

## Suggested metrics

- final normalized-state norm
- normalized settling time
- quadratic LQR-style cost
- integrated squared control effort
- maximum absolute normalized control input
- Lyapunov derivative violation fraction
- finite-horizon convergence count and fraction

## Suggested plots

- position comparison
- control input comparison
- phase portrait comparison
- Lyapunov contour comparison
- finite-horizon convergence comparison
- noise 및 parameter variation 하의 robustness comparison

## Research questions

- KAN controller는 표준 neural network보다 LQR을 더 잘 모방하는가?
- KAN controller는 더 매끄러운 제어 입력을 생성하는가?
- KAN controller는 Lyapunov derivative behavior를 개선하는가?
- 동일한 horizon, tolerance, bounds, grid에서 KAN controller는 finite-horizon convergence fraction을 개선하는가?
- KAN controller는 noise, saturation, parameter changes에서 robust하게 유지되는가?

## Important caution

모델 아키텍처를 바꾸는 것만으로 안정성이 자동 보장되지는 않습니다.

KAN 결과도 simulation, Lyapunov-style grid checks, robustness experiments, finite-horizon convergence analysis로 계속 검증해야 합니다. 이러한 sampled checks만으로는 수학적 attraction region이 성립되지 않습니다.
