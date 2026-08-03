🌐 언어: [English](../en/experiment_log_template.md) | [日本語](../ja/experiment_log_template.md) | [한국어](../ko/experiment_log_template.md) | [ไทย](../th/experiment_log_template.md)

# 실험 로그 Template

## 식별 정보

- 날짜:
- Branch와 commit SHA:
- 연구 질문:
- 목적:

## 환경과 설정

- Python과 PyTorch version:
- Runtime:
- Random seed:
- Epochs, learning rate, dataset size, network architecture:
- Plant, controller, simulation, Lyapunov, noise, parameter 설정:

## 명령과 출력

- 사용 명령:
- Metrics CSV:
- Report:
- Figures:

## 해석

- 무엇이 개선되거나 나빠졌는가?
- LQR과 비교하면 어떠한가?
- 표본 Lyapunov 위반 또는 robustness failure가 있었는가?
- 이전 run과 설정을 비교할 수 있는가?

## 결정

- Reference result로 보관? Yes / No
- Report 또는 presentation에 사용? Yes / No
- 다음 실험:

`python scripts/new_experiment_log.py "short description" --language ko`로 timestamp copy를 만들 수 있습니다.
