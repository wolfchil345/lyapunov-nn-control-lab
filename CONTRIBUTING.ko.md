🌐 언어: [English](CONTRIBUTING.md) | [日本語](CONTRIBUTING.ja.md) | [한국어](CONTRIBUTING.ko.md) | [ไทย](CONTRIBUTING.th.md)

# 기여 가이드

Lyapunov NN Control Lab에 기여해 주셔서 감사합니다. 아래는 코드, 문서, 테스트를 변경할 때 따르는 권장 절차입니다.

## 개발 환경 설정

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## 테스트 실행

```bash
python -m pytest
```

## 실험 실행 (로컬)

```bash
python main.py
```

## 브랜치 워크플로

수정하기 전에 기능 브랜치를 생성하세요。

```bash
git switch main
git pull origin main
git switch -c feature/your-feature-name
```

## 커밋 스타일

짧고 명확한 커밋 메시지를 사용하세요. 예:

- Add noise robustness experiment
- Add reproducibility guide
- Fix Lyapunov metric handling

## 권장 기여 영역

- 새로운 컨트롤러 기준 추가
- 추가적인 강건성 실험
- 플롯 및 문서 개선
- 수치 유틸리티 테스트 추가
- 초보자를 위한 예시 추가

## 변경 제출 전

테스트와 주요 예시를 실행하여 변경이 기존 동작을 훼손하지 않는지 확인하세요。

```bash
python -m pytest
python main.py
```

명령어 및 파일명은 원문과 동일하게 유지되어야 합니다.
