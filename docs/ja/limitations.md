🌐 言語: [English](../en/limitations.md) | [日本語](../ja/limitations.md) | [한국어](../ko/limitations.md) | [ไทย](../th/limitations.md)

# Limitations

このページでは、Lyapunov Neural-Network Control Lab の重要な制約を説明します。

## 教育研究プロジェクト

このリポジトリは、学習、実験、研究探索のために設計されています。

完全な安全認証済み制御システムとして扱うべきではありません。

## 単純化された物理モデル

主要プラントは mass-spring-damper system です。

これは制御実験には有用ですが、多くの実機械システムより大幅に単純です。

## 正規化座標の制約

このモデルは無次元であり、`q`、`v`、`tau`、`u` を SI 単位へ写像する定義を持ちません。したがって結果は normalized simulation の比較を支えますが、metres、seconds、newtons、hardware energy への直接的主張は支えません。

## グリッドベース安定性チェックの制約

Lyapunov checks はサンプルグリッド点で評価されます。

グリッドチェックの合格は、あらゆる状態に対する大域安定性を証明しません。

チェック領域における経験的証拠を与えるだけです。

## neural-network 制御器の制約

neural-network 制御器はデータから学習されるため、学習分布外で挙動が悪化する可能性があります。

LQR を良好に模倣していても、全領域で安定性が自動保証されるわけではありません。

## 数値シミュレーションの制約

シミュレーション結果は solver settings、time step、package versions、数値許容差に依存する可能性があります。

マシン間で小さな差が生じることがあります。

## 有限時間収束の制約

convergence map は、サンプル状態が 1 つの normalized-time horizon において strict criterion `||x(T)||_2 < epsilon` を満たすかどうかのみを判定します。この tolerance は Euclidean normalized-state tolerance です。結果は horizon、tolerance、grid bounds、resolution に依存します。このテストの失敗は、その状態が数学的 attraction region 外にあることを示しません。逆に合格しても、asymptotic convergence を認証しません。

別途行う sampled Lyapunov checks も、形式的 continuous-state attraction-region certificate を生成しません。Lyapunov sublevel set は、描画しただけでは認証されません。

## ロバスト性実験の制約

noise、saturation、parameter variation 実験は、選択したケースのみをテストします。

あらゆる不確かさや外乱を網羅してはいません。

## Lyapunov 関数の制約

このプロジェクトは、システム設定に基づく quadratic Lyapunov-style 解析を使用します。

より高度な非線形システムでは、学習型、非二次、あるいは問題固有の Lyapunov 関数が必要になる場合があります。

## 将来の改善方向

- neural-network 制御器の formal verification を追加する。
- より大規模かつ非線形なシステムを試験する。
- より多くの制御器タイプを比較する。
- neural Lyapunov functions を直接学習する。
- robustness と不確かさ解析を強化する。
- actuator saturation 以外の safety constraints を検討する。
