🌐 언어: [English](../en/result_review_checklist.md) | [日本語](../ja/result_review_checklist.md) | [한국어](../ko/result_review_checklist.md) | [ไทย](../th/result_review_checklist.md)

# Result Review Checklist

이 checklist는 생성된 result files를 report, presentation, thesis chapter, portfolio에 사용하기 전에 점검할 때 사용합니다.

## 1. 실험 설정 확인

- controller type이 명확하다
- random seed가 기록되어 있다
- number of epochs가 기록되어 있다
- Lyapunov grid size가 기록되어 있다
- finite-horizon convergence 결과에 horizon, strict final-state tolerance, bounds, resolution, tested count, converged count가 기록되어 있다
- noise 또는 parameter variation 설정이 기록되어 있다

## 2. 생성 파일 확인

다음을 실행합니다.

```bash
python scripts/list_results.py
```

중요 파일 이름이 명확하고 올바른 실험과 연결되어 있는지 확인합니다.

## 3. 플롯 리뷰

- 안정이 기대되는 경우 궤적이 원점으로 이동한다
- 설명되지 않은 이상 스파이크가 control signals에 없다
- 비교 플롯에서 LQR, neural network, 기타 controllers 라벨이 명확하다
- figures가 slides/report에서 읽기 충분하다

## 4. metrics 리뷰

- metrics는 설정이 호환되는 실험끼리만 비교한다
- 낮은 cost 또는 error만으로 안정성 증명으로 간주하지 않는다
- control effort는 tracking/stabilization quality와 함께 본다

## 5. Lyapunov 관련 출력 리뷰

- grid-based checks를 sampled evidence로 설명한다
- 실제 formal proof가 없는 한 global proof를 주장하지 않는다
- 문제 사례를 숨기지 않고 기록/설명한다

## 6. finite-horizon convergence 출력 리뷰

- percentages를 horizon, tolerance, sampled grid와 함께 보고한다
- finite-time pass를 formal attraction region이라고 부르지 않는다
- finite-time failure를 asymptotic divergence 근거로 취급하지 않는다
- convergence map과 sampled Lyapunov checks를 개념적으로 분리한다

## 7. robustness 출력 리뷰

- noise level 또는 parameter variation을 명확히 쓴다
- failed cases를 기록한다
- robustness results를 baseline results와 라벨 없이 섞지 않는다

## 8. 결과 commit 전

다음을 실행합니다.

```bash
python scripts/check_environment.py
make checks
python scripts/list_results.py
git status
```

result files는 유용한 예시, 최종 artifacts, 문서화에 필요한 경우에만 commit합니다.

## 최종 규칙

중요한 결과는 file name, experiment log, 관련 문서만으로 이해 가능해야 합니다.
