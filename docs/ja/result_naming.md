🌐 言語: [English](../en/result_naming.md) | [日本語](../ja/result_naming.md) | [한국어](../ko/result_naming.md) | [ไทย](../th/result_naming.md)

# 結果ファイルの命名

小文字の英数字とアンダースコアを使用します。

```text
YYYYMMDD_controller_experiment_setting.ext
```

例:

```text
20260804_nn_trajectory_seed7.png
20260804_comparison_roa_grid15.csv
20260804_nn_noise_sigma005.md
```

日付、制御器、実験の種類、結果を区別できる設定を名前に含めます。空白や `final.png`、`new_result.csv`、`really_final_plot.png` のような曖昧な名前は避けてください。

`main.py` が使う追跡対象の参照成果物は、安定したファイル名を維持します。追加実行には拡張した命名パターンを使用し、重要な出力は実験ログからリンクします。
