🌐 언어: [English](../en/result_naming.md) | [日本語](../ja/result_naming.md) | [한국어](../ko/result_naming.md) | [ไทย](../th/result_naming.md)

# 결과 파일 이름

소문자 영어 identifier와 underscore를 사용합니다.

```text
YYYYMMDD_controller_experiment_setting.ext
```

예:

```text
20260804_nn_trajectory_seed7.png
20260804_comparison_roa_grid15.csv
20260804_nn_noise_sigma005.md
```

날짜, controller, experiment type, 결과를 구분하는 setting을 포함합니다. 공백과 `final.png`, `new_result.csv`, `really_final_plot.png` 같은 이름은 피합니다.

`main.py`가 사용하는 추적 reference artifact는 안정된 filename을 유지합니다. 추가 run에는 확장 pattern을 사용하고 중요한 출력은 experiment log에서 연결합니다.
