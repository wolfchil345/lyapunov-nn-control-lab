🌐 언어: [English](../en/environment.md) | [日本語](../ja/environment.md) | [한국어](../ko/environment.md) | [ไทย](../th/environment.md)

# 환경 설정

이 가이드는 Lyapunov neural network control lab을 위한 로컬 Python 환경을 준비하는 방법을 설명합니다.

## 권장 Python 버전

Python 3.10 이상을 사용하세요.

## 가상 환경 만들기

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell에서는:

```powershell
.venv\Scripts\Activate.ps1
```

## 프로젝트 설치

일반 사용:

```bash
python -m pip install -e .
```

개발, 테스트, 패키지 빌드:

```bash
python -m pip install -e ".[dev]"
```

## 로컬 검사 실행

```bash
python scripts/run_checks.py
```

이 명령은 문서 링크 검사, 단위 테스트, quick start 예제를 실행합니다.

## 메인 실험 실행

```bash
python main.py
```

## 흔한 문제

- import가 실패하면 리포지토리 루트에서 명령을 실행하고 있는지 확인하세요.
- 런타임 패키지가 없으면 `python -m pip install -e .`를 다시 실행하세요.
- 테스트나 빌드 도구가 없으면 `python -m pip install -e ".[dev]"`를 실행하세요.
- 생성된 결과가 오래돼 보이면 다시 실험하기 전에 results 디렉터리를 정리하세요.

## 환경 확인

Codespaces 또는 로컬 머신에서 의존성 문제가 있을 때 환경 검사기를 사용하세요.

```bash
python scripts/check_environment.py
```

이 검사는 Python, 필요한 프로젝트 파일, 설치된 패키지, 그리고 선언된 런타임 import를 확인합니다.
