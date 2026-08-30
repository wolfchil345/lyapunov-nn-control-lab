🌐 언어: [English](../en/troubleshooting.md) | [日本語](../ja/troubleshooting.md) | [한국어](../ko/troubleshooting.md) | [ไทย](../th/troubleshooting.md)

# 문제 해결 가이드

이 가이드는 Lyapunov Neural-Network Control Lab을 실행할 때 자주 발생하는 문제와 빠른 해결책을 정리합니다.

## `ModuleNotFoundError`

Python이 프로젝트나 런타임 의존성을 찾지 못하면 프로젝트를 설치하세요.

```bash
python -m pip install -e .
```

## 코드 변경 후 테스트 실패

로컬 검사 스크립트를 실행하세요.

```bash
python scripts/run_checks.py
```

테스트 하나만 실패한 경우 첫 번째 오류 메시지를 주의 깊게 읽고 traceback에 나온 파일을 확인하세요.

## 결과가 오래됐거나 혼란스러움

새로운 격리된 run을 만들고 run ID로 선택하세요. 새로운 실험이 필요하다는 이유만으로 이전에 완료된 run을 삭제하지 마세요.

```bash
python main.py
python scripts/list_results.py
```

## CSV 요약이 나타나지 않음

선택한 run 디렉터리 안의 보고서를 사용하세요. 다음으로 확인할 수 있습니다.

```bash
python scripts/verify_run.py results/runs/<run_id>
```

## 플롯이 나타나지 않음

생성된 플롯은 `results/runs/<run_id>/`에 저장됩니다. 파일 탐색기에서 해당 디렉터리를 열거나 다음을 실행하세요.

```bash
find results/runs/<run_id> -maxdepth 1 -type f
```

## 학습 시간이 오래 걸림

메인 실험은 신경망 제어기를 학습하며, 안정성/강건성 실험이나 grid 기반 실험도 함께 실행할 수 있습니다. 머신에 따라 시간이 걸릴 수 있습니다.

빠르게 확인하려면 다음을 실행하세요.

```bash
python examples/quick_start.py
```

## 수치 결과가 조금 달라짐

solver 허용오차, 패키지 버전, 하드웨어 차이로 인해 작은 수치 차이가 생길 수 있습니다.

## Git 브랜치가 헷갈림

현재 브랜치와 로컬 변경 사항을 확인하세요.

```bash
git branch --show-current
git status
```

새 기능을 시작하기 전에 `main`으로 돌아가 최신 버전을 pull 하세요.

```bash
git switch main
git pull origin main
```
