🌐 언어: [English](ROADMAP.md) | [日本語](ROADMAP.ja.md) | [한국어](ROADMAP.ko.md) | [ไทย](ROADMAP.th.md)

# 로드맵

## 단기

- 여러 seed에서 neural training을 반복하고 분포 또는 confidence interval 보고.
- 실험 선택 CLI를 추가하고 비싼 sweep을 집중된 command로 분리.
- 생성 report에 dependency version과 experiment configuration 기록.

## 제어와 강건성

- 호환 setting에서 PID, LQR, MPC, MLP, KAN controller 비교.
- Nonlinear plant, external disturbance, delay, quantization, 더 넓은 uncertainty set 추가.
- Region-of-attraction 해석을 확장하고 failure-case map 보존.

## 안정성 해석

- Alternative 및 learned Lyapunov function 시험.
- Candidate violation 근처에 adaptive sampling 추가.
- Empirical grid check와 formal neural-network verification tool 비교.

## 물리 검증

- 실제 장비 운용 전 hardware-in-the-loop stage 구축.
- Actuator, sensor, safety constraint 명시.
- Safety-certified component와 research prototype 분리.

## 커뮤니케이션

- Feature 변경에도 네 언어 documentation 완전성 유지.
- 같은 reproducible result에 기반한 poster와 짧은 technical article 추가.

장기 목표는 신뢰할 수 있는 learning-based control 실험 platform이며 하나의 neural controller가 control safety 전반을 해결한다는 주장이 아닙니다.
