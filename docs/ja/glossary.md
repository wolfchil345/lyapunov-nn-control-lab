🌐 言語: [English](../en/glossary.md) | [日本語](../ja/glossary.md) | [한국어](../ko/glossary.md) | [ไทย](../th/glossary.md)

# 用語集

- **State（状態）**: システムを表す変数。本プロジェクトでは位置と速度。
- **Plant（プラント）**: 制御される物理またはsimulation system。
- **Control input（制御入力）**: Plantへ加えるforce command `u`。
- **Closed loop（閉ループ）**: State feedbackで接続されたcontrollerとplant。
- **LQR**: Linear Quadratic Regulator。古典的baselineおよびteacher。
- **Equilibrium（平衡点）**: 変化しない状態。目標は原点。
- **Lyapunov function**: 安定性を調べる正のenergy-like function。
- **Lyapunov derivative**: 軌道に沿った変化率 `V_dot`。
- **Actuator saturation**: 実現可能なcontrol inputの制限。
- **Region of attraction**: 明示された条件で平衡点へ収束するinitial state集合。
- **Imitation learning**: Teacher actionを再現するmodel学習。
- **Stability-aware training**: サンプルLyapunov penaltyを含む学習。
- **Ablation study**: 一つの設計要素だけを変える比較。

Code identifierと数式記号は全翻訳で英語のまま維持します。
