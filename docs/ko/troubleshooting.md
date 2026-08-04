🌐 언어: [English](../en/troubleshooting.md) | [日本語](../ja/troubleshooting.md) | [한국어](../ko/troubleshooting.md) | [ไทย](../th/troubleshooting.md)

# 문제 해결

## 모듈 불러오기 또는 테스트 실패

터미널이 저장소 루트인지 확인하고 `.venv`를 활성화한 뒤 `python -m pip install -e ".[dev]"`와 `python -m pytest`를 실행합니다.

## 그래프 또는 CSV가 오래됨

`git status`를 확인하고 추적 산출물을 백업합니다. `python scripts/clean_results.py`로 삭제 대상을 미리 확인한 뒤 `python scripts/clean_results.py --yes`와 `python main.py`를 실행합니다.

## 수치가 조금 다름

Python 버전, 의존성 버전, 고정 시드를 확인합니다. 플랫폼에 따른 작은 차이는 발생할 수 있지만, 큰 차이는 원인을 조사해야 합니다.

## 학습이 느림

환경 설정 확인에는 빠른 시작 예제를 사용합니다. 전체 실험에는 학습, 강인성 범위 평가, 흡인 영역 시뮬레이션이 포함됩니다.

## Git 브랜치 혼동

`git status -sb`와 `git branch --show-current`를 실행합니다. 환경 파일이나 관련 없는 생성 결과를 커밋하지 마십시오.

설치 관련 문제는 [의존성 문제 해결](dependency_troubleshooting.md)을 참고하십시오.
