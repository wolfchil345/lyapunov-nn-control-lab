🌐 언어: [English](../en/onboarding.md) | [日本語](../ja/onboarding.md) | [한국어](../ko/onboarding.md) | [ไทย](../th/onboarding.md)

# 온보딩 가이드

## 첫 한 시간

1. 한국어 README와 [프로젝트 요약](project_summary.md)을 읽습니다.
2. [환경 설정 가이드](environment.md)를 따릅니다.
3. `python examples/quick_start.py`를 실행합니다.
4. `make checks`를 실행하고 `results/`를 확인합니다.
5. [방법론](methodology.md), [실험 워크플로](experiment_workflow.md), [한계](limitations.md)를 읽습니다.

## 코드 변경 전

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/short-description
```

과학적 변경과 문서 변경을 분리하고 실험 설정을 기록하며 검토 요청 전에 `make quality-gate`를 실행합니다.

전체 절차는 [Git 워크플로](git_workflow.md)와 [기여 가이드](../../CONTRIBUTING.ko.md)를 참고하십시오.
