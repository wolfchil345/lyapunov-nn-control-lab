🌐 언어: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# 의존성 문제 해결

이 가이드는 의존성과 환경에서 자주 발생하는 문제를 해결하는 방법을 설명합니다.

## 첫 진단 명령

패키지를 바꾸기 전에 환경 검사기를 실행하세요.

```bash
python scripts/check_environment.py
```

## PyTorch import 오류

PyTorch import가 shared library 오류로 실패하면 CPU wheel을 다시 설치하세요.

```bash
python -m pip uninstall -y torch torchvision torchaudio
python -m pip cache purge
python -m pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
python -c "import torch; print(torch.__version__)"
```

PyTorch를 다시 설치한 뒤 다음을 실행하세요.

```bash
python scripts/check_environment.py
python scripts/run_checks.py
```

## 의존성 재설정

가상 환경이 지저분해졌다면 다시 만드세요.

```bash
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python scripts/run_checks.py
```

## Codespaces 재설정

Codespaces가 이상하게 동작하면 Codespaces 명령 팔레트에서 컨테이너를 다시 빌드하세요.

다시 빌드한 뒤 다음을 실행하세요.

```bash
python scripts/check_environment.py
python scripts/run_checks.py
```

## 도움을 요청할 때

체크가 계속 실패하면 첫 FAIL 줄부터 끝까지의 터미널 출력을 그대로 복사하세요.
