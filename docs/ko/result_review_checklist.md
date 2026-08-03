🌐 언어: [English](../en/result_review_checklist.md) | [日本語](../ja/result_review_checklist.md) | [한국어](../ko/result_review_checklist.md) | [ไทย](../th/result_review_checklist.md)

# 결과 Review Checklist

## 설정

- [ ] Branch, commit, seed, epochs, model architecture를 기록했다.
- [ ] Initial condition, duration, grid density, noise, parameter case를 기록했다.
- [ ] 비교 run은 의도한 변수만 다르다.

## 출력

- [ ] 예상 CSV, report, model, figure가 존재한다.
- [ ] Figure label을 읽을 수 있고 궤적이 타당하다.
- [ ] Metric이 유한하며 여러 지표를 함께 해석한다.
- [ ] Saturation, noise, parameter case가 명확히 표시된다.

## 안정성 주장

- [ ] 표본 Lyapunov check를 경험적 근거로 설명한다.
- [ ] Region-of-attraction 주장에 test grid, horizon, threshold를 명시한다.
- [ ] Failure case와 예상 밖 거동을 유지하고 설명한다.

## Commit 전

- [ ] `make quality-gate`가 pass한다.
- [ ] `git diff`에 의도한 artifact만 있다.
- [ ] Documentation과 experiment log가 생성 결과와 일치한다.
