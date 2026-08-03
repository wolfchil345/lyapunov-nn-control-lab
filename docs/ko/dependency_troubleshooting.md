🌐 언어: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# 의존성 문제 해결

먼저 다음을 실행합니다.

```bash
python scripts/check_environment.py
python -m pip check
```

## Package 누락 또는 PyTorch import error

`.venv`를 활성화하고 pip를 upgrade한 뒤 `python -m pip install -e .`로 다시 설치합니다. system Python과 virtual environment package를 섞지 마십시오.

## Git LFS error

Git LFS를 설치하고 `git lfs install`, `git lfs pull`을 실행해 추적 binary asset을 복원합니다.

## Clean reset

system interpreter를 바꾸지 말고 새 virtual environment를 만듭니다. Codespaces에서 문제가 계속되면 dev container를 rebuild합니다.

도움을 요청할 때 `python scripts/check_environment.py`, `python --version`, `python -m pip check` 출력을 포함하십시오.
