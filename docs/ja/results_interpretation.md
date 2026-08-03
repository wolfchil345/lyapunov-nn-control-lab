🌐 言語: [English](../en/results_interpretation.md) | [日本語](../ja/results_interpretation.md) | [한국어](../ko/results_interpretation.md) | [ไทย](../th/results_interpretation.md)

# 結果の解釈

## 性能指標

- `final_state_norm`: 最終時刻における目標平衡点からの距離。
- `settling_time_s`: 以後、状態が閾値内に留まる最初の時刻。
- `quadratic_cost`: LQR形式の状態・制御penaltyの積分。
- `control_energy`: 制御入力二乗の積分。
- `max_abs_control`: 最大絶対actuator command。

単一のmetricだけでは安定性や制御器品質を示せません。収束、入力努力、cost、robustnessを合わせて比較します。

## 安定性の証拠

サンプル点で負の `V_dot` は評価grid内の局所的減少を支持しますが、grid間、領域外、未試験の不確かさを証明しません。

## ロバスト性と引き込み領域

Noise、parameter variation、actuator saturationはscenario testです。Region-of-attraction mapは選択したhorizonとthresholdでサンプル初期条件のみを分類します。

## 読む順序

1. 設定とseedを確認。
2. 軌道と制御制限を確認。
3. 定量metricを比較。
4. Lyapunovとregion-of-attraction診断を確認。
5. [制約](limitations.md)を読み、failure caseを記録。
