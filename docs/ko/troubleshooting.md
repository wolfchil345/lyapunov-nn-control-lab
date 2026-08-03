🌐 언어: [English](../en/troubleshooting.md) | [日本語](../ja/troubleshooting.md) | [한국어](../ko/troubleshooting.md) | [ไทย](../th/troubleshooting.md)

# 문제 해결

## Import 또는 test 실패

terminal이 저장소 root인지 확인하고 `.venv`를 활성화한 뒤 `python -m pip install -e .`와 `python -m pytest`를 실행합니다.

## Plot 또는 CSV가 오래됨

`git status`를 확인하고 추적 artifact를 backup합니다. 그 다음에만 `python scripts/clean_results.py`와 `python main.py`를 실행합니다.

## 수치가 조금 다름

Python, dependency version, 고정 seed를 확인합니다. 작은 platform 차이는 가능하지만 큰 차이는 조사해야 합니다.

## 학습이 느림

설정 확인에는 quick start를 사용합니다. 전체 실험에는 학습, robustness sweep, region-of-attraction simulation이 포함됩니다.

## Git branch 혼동

`git status -sb`와 `git branch --show-current`를 실행합니다. 환경 파일이나 관련 없는 생성 결과를 commit하지 마십시오.

설치 관련 문제는 [의존성 문제 해결](dependency_troubleshooting.md)을 참고하십시오.
