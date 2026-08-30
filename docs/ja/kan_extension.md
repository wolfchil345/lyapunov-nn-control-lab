🌐 言語: [English](../en/kan_extension.md) | [日本語](../ja/kan_extension.md) | [한국어](../ko/kan_extension.md) | [ไทย](../th/kan_extension.md)

# KAN Extension ガイド

このガイドでは、現在の Lyapunov Neural-Network Control Lab を Kolmogorov-Arnold Network 制御器実験へ拡張する方法を説明します。

## Motivation

現在のプロジェクトでは、標準 neural-network 制御器で LQR を模倣し、安定性関連の挙動を評価しています。

KAN-based 制御器は、システム状態から制御入力への写像に対する代替の function approximator として試験できます。

## Current controller pipeline

現在のワークフローは次のとおりです。

1. mass-spring-damper system を定義する。
2. LQR 制御器から学習データを生成する。
3. neural-network 制御器を学習する。
4. 閉ループ挙動をシミュレーションする。
5. performance metrics を計算する。
6. Lyapunov-style stability behavior を確認する。
7. robustness 実験と finite-horizon convergence 実験を実行する。

## KAN controller idea

KAN 制御器では、標準 neural-network モデルを KAN-style モデルに置き換えます。

入力は引き続きシステム状態です。

- position
- velocity

出力も引き続き制御入力です。

- normalized scalar control input

## Files that may need changes

### `src/controllers.py`
KAN controller class または wrapper function を追加する。

### `main.py`
LQR と現行 neural-network controller に加えて、KAN の学習、シミュレーション、metrics、plotting を追加する。

### `src/plotting.py`
LQR、標準 neural network、KAN を比較する plots を追加する。

### `tests/`
KAN controller が有効な scalar control を返し、simulation で実行できることを確認する tests を追加する。

## Suggested experiment design

次の 3 つの制御器を比較します。

- LQR baseline
- standard neural-network controller
- KAN controller

すべての制御器で同じ初期状態、metrics、Lyapunov checks を使用します。

## Suggested metrics

- final normalized-state norm
- normalized settling time
- quadratic LQR-style cost
- integrated squared control effort
- maximum absolute normalized control input
- Lyapunov derivative violation fraction
- finite-horizon convergence count and fraction

## Suggested plots

- position comparison
- control input comparison
- phase portrait comparison
- Lyapunov contour comparison
- finite-horizon convergence comparison
- noise と parameter variation 下の robustness comparison

## Research questions

- KAN controller は標準 neural network より良く LQR を模倣できるか。
- KAN controller はより滑らかな制御入力を生成するか。
- KAN controller は Lyapunov derivative behavior を改善するか。
- KAN controller は同じ horizon、tolerance、bounds、grid で finite-horizon convergence fraction を改善するか。
- KAN controller は noise、saturation、parameter changes 下でも robust に保たれるか。

## Important caution

モデルアーキテクチャを置き換えるだけでは、自動的に安定性は保証されません。

KAN 結果も、simulation、Lyapunov-style grid checks、robustness experiments、finite-horizon convergence analysis で確認する必要があります。これらの sampled checks のみでは数学的 attraction region は確立されません。
