🌐 언어: [English](../en/commands.md) | [日本語](../ja/commands.md) | [한국어](../ko/commands.md) | [ไทย](../th/commands.md)

# 명령어 치트 시트

이 페이지는 Lyapunov Neural-Network Control Lab을 실행하고 유지보수할 때 유용한 명령을 모아 놓았습니다.

## 설정

개발 도구를 포함해 프로젝트를 설치합니다.

```bash
python -m pip install -e ".[dev]"
```

## 빠른 시작

초보자용 작은 예제를 실행합니다.

```bash
python examples/quick_start.py
```

## 로컬 검사를 모두 실행

테스트와 빠른 시작 예제를 실행합니다.

```bash
python scripts/run_checks.py
```

## 테스트만 실행

```bash
python -m pytest
```

## 메인 실험 실행

```bash
python main.py
```

## 생성된 결과 요약

```bash
python scripts/summarize_results.py
```

## provenance-aware run 검증

```bash
python scripts/verify_run.py results/runs/<run_id>
```

## 불완전한 staging 디렉터리 정리

```bash
python scripts/clean_results.py
```

## 현재 Git 브랜치 확인

```bash
git branch --show-current
git status
```

## 새 기능 브랜치 시작

```bash
git switch main
git pull origin main
git switch -c feature/my-new-feature
```

## 기능 브랜치를 커밋하고 push

```bash
git add .
git commit -m "Describe the change"
git push -u origin feature/my-new-feature
```

## 기능 브랜치를 main에 병합

```bash
git switch main
git pull origin main
git merge --no-ff feature/my-new-feature
python scripts/run_checks.py
git push origin main
```

## Makefile 단축 명령

이 저장소에는 자주 쓰는 명령 단축키를 모아 둔 `Makefile`이 있습니다.

```bash
make check-env
make checks
make test
make quickstart
make experiment
make clean
make summarize
make verify-run RUN_DIR=results/runs/<run_id>
```

## CI 명령

GitHub Actions는 `make checks`를 사용해 개발 중에 사용하는 것과 같은 로컬 검사를 실행합니다.
