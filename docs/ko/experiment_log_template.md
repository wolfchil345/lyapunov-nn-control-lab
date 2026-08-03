🌐 언어: [English](../en/experiment_log_template.md) | [日本語](../ja/experiment_log_template.md) | [한국어](../ko/experiment_log_template.md) | [ไทย](../th/experiment_log_template.md)

# 실험 로그 양식

## 기본 정보

- 날짜:
- 브랜치와 커밋 SHA:
- 연구 질문:
- 목적:

## 환경과 설정

- Python과 PyTorch 버전:
- 실행 환경:
- 난수 시드:
- 에포크 수, 학습률, 데이터셋 크기, 네트워크 구조:
- 플랜트, 제어기, 시뮬레이션, Lyapunov, 잡음, 매개변수 설정:

## 명령과 출력

- 사용한 명령:
- 평가 지표 CSV:
- 보고서:
- 그림:

## 결과 해석

- 무엇이 개선되었고 무엇이 나빠졌는가?
- 제어기는 LQR과 비교해 어떤 거동을 보였는가?
- 표본점에서 Lyapunov 조건 위반이나 강인성 실패가 있었는가?
- 이 설정은 이전 실험과 비교 가능한가?

## 판단

- 참조 결과로 보존할가? 예 / 아니요
- 보고서나 발표에 사용할가? 예 / 아니요
- 다음 실험:

`python scripts/new_experiment_log.py "short description" --language ko`로 시각이 포함된 사본을 만들 수 있습니다.
