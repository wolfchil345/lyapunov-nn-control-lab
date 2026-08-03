🌐 言語: [English](../en/results_interpretation.md) | [日本語](../ja/results_interpretation.md) | [한국어](../ko/results_interpretation.md) | [ไทย](../th/results_interpretation.md)

# 結果の解釈

## 性能指標

- `final_state_norm`: 最終時刻における目標平衡点からの距離。
- `settling_time_s`: 以後、状態が閾値内に留まる最初の時刻。
- `quadratic_cost`: LQR形式の状態・制御ペナルティの積分。
- `control_energy`: 制御入力二乗の積分。
- `max_abs_control`: 最大絶対アクチュエータ コマンド。

単一の指標だけでは安定性や制御器品質を示せません。収束、入力努力、コスト、ロバスト性を合わせて比較します。

## 安定性の証拠

サンプル点で負の `V_dot` は評価グリッド内の局所的減少を支持しますが、グリッド間、領域外、未試験の不確かさを証明しません。

## ロバスト性と引き込み領域

ノイズ、パラメータ変動、アクチュエータ飽和はシナリオ試験です。引き込み領域マップは選択した評価時間と閾値でサンプル初期条件のみを分類します。

## 読む順序

1. 設定とシードを確認。
2. 軌道と制御制限を確認。
3. 定量指標を比較。
4. Lyapunovと引き込み領域診断を確認。
5. [制約](limitations.md)を読み、失敗事例を記録。
