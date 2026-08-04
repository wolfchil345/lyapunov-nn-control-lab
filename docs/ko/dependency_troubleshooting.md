🌐 언어: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# 의존성 문제 해결

먼저 다음을 실행하세요.

```bash
python scripts/check_environment.py
python -m pip check
```

## 패키지가 없거나 PyTorch를 불러오지 못할 때

`.venv`를 활성화하고 pip를 업그레이드한 뒤 `python -m pip install -e ".[dev]"`로 프로젝트를 다시 설치하세요. 시스템 Python과 가상 환경의 패키지를 섞어 사용하지 마세요.

## 패키지 정보 또는 import 오류

`python scripts/check_package.py`를 실행하세요. 실패하면 개발 extra가 포함된 편집 가능 프로젝트를 다시 설치하세요. 현재 추적하는 산출물에는 Git LFS가 필요하지 않습니다.

## 환경 재생성

시스템 Python을 수정하지 말고 새 가상 환경을 만드세요. Codespaces에서 환경의 불일치가 계속되면 개발 컨테이너를 다시 빌드하세요.

도움을 요청할 때는 `python scripts/check_environment.py`, `python --version`, `python -m pip check`의 출력을 함께 제공하세요.
