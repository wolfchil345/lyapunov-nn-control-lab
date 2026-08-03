🌐 言語: [English](../en/result_naming.md) | [日本語](../ja/result_naming.md) | [한국어](../ko/result_naming.md) | [ไทย](../th/result_naming.md)

# 結果ファイルの命名

小文字英語identifierとunderscoreを使用します。

```text
YYYYMMDD_controller_experiment_setting.ext
```

例:

```text
20260804_nn_trajectory_seed7.png
20260804_comparison_roa_grid15.csv
20260804_nn_noise_sigma005.md
```

日付、controller、experiment type、結果を区別するsettingを含めます。Spaceや `final.png`、`new_result.csv`、`really_final_plot.png` は避けます。

`main.py` が使う追跡reference artifactは安定したfilenameを維持します。追加runには拡張patternを使用し、重要な出力をexperiment logからlinkします。
