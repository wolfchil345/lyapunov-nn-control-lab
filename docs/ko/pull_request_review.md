🌐 언어: [English](../en/pull_request_review.md) | [日本語](../ja/pull_request_review.md) | [한국어](../ko/pull_request_review.md) | [ไทย](../th/pull_request_review.md)

# Pull Request Review 가이드

이 가이드는 변경 사항을 `main`에 병합하기 전에 어떻게 검토하는지 설명합니다.

## 검토 목표

- 변경 목적이 명확한지 확인합니다.
- 로컬 체크가 통과하는지 확인합니다.
- 동작이 바뀌면 문서가 업데이트되었는지 확인합니다.
- 실험 결과가 실수로 덮어써지지 않았는지 확인합니다.
- 생성된 파일이 의도적으로 포함되었는지 또는 무시되었는지 확인합니다.

## 병합 전 로컬 명령

```bash
python scripts/check_environment.py
make checks
git status
```

## 검토 체크리스트

pull request 또는 feature branch를 병합하기 전에 다음을 확인합니다.

- branch 이름이 변경 내용을 설명하는지.
- commit message가 명확한지.
- 테스트가 로컬에서 통과하는지.
- GitHub Actions가 통과하는지.
- 필요하다면 README 또는 docs가 업데이트되었는지.
- result files는 유용한 예시 또는 최종 산출물일 때만 commit되는지.

## 연구용 검토 항목

- 변경이 numerical results에 영향을 주는가.
- 변경이 Lyapunov analysis에 영향을 주는가.
- 변경이 reproducibility에 영향을 주는가.
- 변경이 random seeds, model architecture, experiment settings를 바꾸는가.

## 병합 규칙

체크가 통과하고 working tree가 clean할 때만 병합합니다.
