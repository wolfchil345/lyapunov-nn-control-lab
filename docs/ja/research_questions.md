🌐 言語: [English](../en/research_questions.md) | [日本語](../ja/research_questions.md) | [한국어](../ko/research_questions.md) | [ไทย](../th/research_questions.md)

# 研究課題

このドキュメントは、Lyapunov Neural-Network Control Lab における研究課題候補をまとめたものです。

## 主研究課題

neural-network 制御器は、閉ループシミュレーションにおいて有用な Lyapunov-style 安定挙動を維持しながら、LQR 制御器を模倣できるか。

## 制御性能

- neural-network 制御器の性能は LQR baseline にどれだけ近いか。
- neural-network 制御器は final normalized-state norm を安定して低減できるか。
- normalized settling time、quadratic LQR-style cost、integrated squared control effort は制御器間でどう比較されるか。

## 安定挙動

- Lyapunov derivative はチェック領域で概ね負を維持するか。
- サンプル初期状態のうち、有限時間後に指定 final-state tolerance を満たすのはどれか。
- その finite-horizon 率は horizon、tolerance、bounds、grid resolution にどれだけ敏感か。

## ロバスト性挙動

- measurement noise は neural-network 制御器にどう影響するか。
- actuator saturation は収束にどう影響するか。
- normalized mass、damping、stiffness 係数変化に対して制御器はどれだけ敏感か。

## 学習設計

- stability penalty weight は模倣精度にどう影響するか。
- stability penalty weight は Lyapunov derivative violations にどう影響するか。
- imitation loss と stability-aware behavior の間に有用な trade-off はあるか。

## KAN 拡張に関する課題

- KAN 制御器は標準 neural network と同等またはそれ以上に LQR を模倣できるか。
- KAN 制御器はより滑らか、あるいはより解釈しやすい制御挙動を生むか。
- 同一 sampling settings 下で KAN 制御器は robustness や finite-horizon convergence 結果を改善するか。

## 可能な卒業研究方向

可能な卒業研究方向として、同一の Lyapunov-style 評価パイプラインで標準 neural-network 制御器と KAN-based 制御器を比較することが挙げられます。

## 推奨評価サマリー

各制御器について、次を報告します。

- performance metrics
- Lyapunov grid-check results
- robustness results
- finite-horizon convergence の件数、割合、sampling metadata
- limitations と failure cases
