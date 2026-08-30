🌐 언어: [English](../en/limitations.md) | [日本語](../ja/limitations.md) | [한국어](../ko/limitations.md) | [ไทย](../th/limitations.md)

# Limitations

이 페이지는 Lyapunov Neural-Network Control Lab의 중요한 한계를 설명합니다.

## 교육 연구 프로젝트

이 저장소는 학습, 실험, 연구 탐색을 위해 설계되었습니다.

완전한 안전 인증 제어 시스템으로 간주해서는 안 됩니다.

## 단순 물리 모델

주요 플랜트는 mass-spring-damper system입니다.

제어 실험에는 유용하지만, 많은 실제 기계 시스템보다 훨씬 단순합니다.

## 정규화 좌표 한계

모델은 무차원이며 `q`, `v`, `tau`, `u`를 SI 단위로 매핑하는 정의가 없습니다. 따라서 결과는 normalized simulation 비교를 지원하지만 metres, seconds, newtons, hardware energy에 대한 직접 주장까지는 지원하지 않습니다.

## 격자 기반 안정성 점검 한계

Lyapunov checks는 샘플 격자점에서 평가됩니다.

격자 점검 통과는 가능한 모든 상태에 대한 전역 안정성을 증명하지 않습니다.

점검된 영역에서의 경험적 증거만 제공합니다.

## neural-network 제어기 한계

neural-network 제어기는 데이터로 학습되므로 학습 분포 밖에서는 성능이 나빠질 수 있습니다.

LQR을 잘 모방해도 모든 영역에서 안정성이 자동 보장되지는 않습니다.

## 수치 시뮬레이션 한계

시뮬레이션 결과는 solver settings, time step 선택, package versions, numerical tolerances에 영향을 받을 수 있습니다.

머신 간에 작은 차이가 생길 수 있습니다.

## 유한 시간 수렴 한계

convergence map은 샘플 상태가 하나의 normalized-time horizon에서 strict criterion `||x(T)||_2 < epsilon`을 만족하는지만 검사합니다. 이 tolerance는 Euclidean normalized-state tolerance입니다. 결과는 horizon, tolerance, grid bounds, resolution에 의존합니다. 이 테스트 실패는 어떤 상태가 수학적 attraction region 밖임을 뜻하지 않으며, 통과 역시 asymptotic convergence를 인증하지 않습니다.

별도의 sampled Lyapunov checks 또한 형식적인 continuous-state attraction-region certificate를 만들지 않습니다. Lyapunov sublevel set은 단지 플로팅했다는 이유만으로 인증되지 않습니다.

## 강건성 실험 한계

noise, saturation, parameter variation 실험은 선택된 경우만 테스트합니다.

가능한 모든 불확실성이나 외란을 다루지는 않습니다.

## Lyapunov 함수 한계

프로젝트는 시스템 설정에 기반한 quadratic Lyapunov-style 분석을 사용합니다.

더 고급 비선형 시스템은 학습형, 비이차형, 혹은 문제 특화 Lyapunov 함수가 필요할 수 있습니다.

## 향후 개선 방향

- neural-network 제어기에 대한 formal verification 추가
- 더 크고 비선형적인 시스템 시험
- 더 많은 제어기 유형 비교
- neural Lyapunov functions 직접 학습
- 더 강한 강건성 및 불확실성 분석 추가
- actuator saturation을 넘어선 safety constraints 연구
