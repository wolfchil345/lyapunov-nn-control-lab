🌐 언어: [English](../en/quality_gate.md) | [日本語](../ja/quality_gate.md) | [한국어](../ko/quality_gate.md) | [ไทย](../th/quality_gate.md)

# Quality Gate

최종 readiness check 실행:

```bash
make quality-gate
```

Project status, workflow badge validation, environment check, result inventory, Markdown link check, 전체 test suite, quick-start example을 실행합니다.

## 사용 전

- Pull request를 open하거나 merge하기 전.
- 추적 experiment result를 교체하기 전.
- Demo, submission, release 전.

## Failure 처리

처음 실패한 command를 읽고 원인을 고친 뒤 gate를 다시 실행합니다. 실패 stage를 skip하거나 변경 범위를 불필요하게 넓히지 마십시오. Pass는 repository consistency를 확인하지만 implemented test를 넘는 과학적 주장을 검증하지는 않습니다.

GitHub Actions는 `.github/workflows/quality-gate.yml`에서 같은 command를 실행합니다.
