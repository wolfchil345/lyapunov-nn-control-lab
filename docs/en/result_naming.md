🌐 Language: [English](../en/result_naming.md) | [日本語](../ja/result_naming.md) | [한국어](../ko/result_naming.md) | [ไทย](../th/result_naming.md)

# Result File Naming

Use lowercase English identifiers with underscores:

```text
YYYYMMDD_controller_experiment_setting.ext
```

Examples:

```text
20260804_nn_trajectory_seed7.png
20260804_comparison_roa_grid15.csv
20260804_nn_noise_sigma005.md
```

Include the date, controller, experiment type, and the setting that makes the result distinct. Avoid spaces and names such as `final.png`, `new_result.csv`, or `really_final_plot.png`.

Keep the stable filenames used by `main.py` for tracked reference artifacts. Use the extended pattern for additional experiment runs and link important outputs from the experiment log.
