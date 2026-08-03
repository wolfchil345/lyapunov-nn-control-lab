🌐 언어: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# 의존성 문제 해결

먼저 다음을 실행하세요.

```bash
python scripts/check_environment.py
python -m pip check
```

## 패키지가 없거나 PyTorch를 불러오지 못할 때

`.venv`를 활성화하고 pip를 업그레이드한 뒤 `python -m pip install -e .`로 프로젝트를 다시 설치하세요. 시스템 Python과 가상 환경의 패키지를 섞어 사용하지 마세요.

## Git LFS 오류

Git LFS를 설치하고 `git lfs install`을 실행하세요. 추적 중인 바이너리 산출물은 `git lfs pull`로 복원할 수 있습니다.

## 환경 재생성

시스템 Python을 수정하지 말고 새 가상 환경을 만드세요. Codespaces에서 환경의 불일치가 계속되면 개발 컨테이너를 다시 빌드하세요.

도움을 요청할 때는 `python scripts/check_environment.py`, `python --version`, `python -m pip check`의 출력을 함께 제공하세요.
