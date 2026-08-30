🌐 言語: [English](../en/troubleshooting.md) | [日本語](../ja/troubleshooting.md) | [한국어](../ko/troubleshooting.md) | [ไทย](../th/troubleshooting.md)

# トラブルシューティングガイド

このガイドでは、Lyapunov Neural-Network Control Lab を実行するときによく起きる問題と、その簡単な対処法をまとめます。

## `ModuleNotFoundError`

Python がプロジェクトや実行時依存関係を見つけられない場合は、プロジェクトをインストールします。

```bash
python -m pip install -e .
```

## コード変更後にテストが失敗する

ローカルチェック用スクリプトを実行します。

```bash
python scripts/run_checks.py
```

1 つのテストだけが失敗した場合は、最初のエラーメッセージを注意深く読み、traceback に出てくるファイルを確認してください。

## 結果が古い、または分かりにくい

新しい独立した run を作成し、run ID で選択してください。新しい実験が必要だからといって、古い完了済みの run を削除しないでください。

```bash
python main.py
python scripts/list_results.py
```

## CSV の要約が表示されない

選択した run ディレクトリ内のレポートを使います。次で検証できます。

```bash
python scripts/verify_run.py results/runs/<run_id>
```

## 図が表示されない

生成された図は `results/runs/<run_id>/` に保存されます。ファイルエクスプローラーでそのディレクトリを開くか、次を実行してください。

```bash
find results/runs/<run_id> -maxdepth 1 -type f
```

## 学習に時間がかかる

メイン実験ではニューラルネットワーク制御器を学習し、さらにロバスト性実験やグリッドベースの実験を行う場合があります。機械によっては時間がかかります。

手早く確認するには次を実行します。

```bash
python examples/quick_start.py
```

## 数値結果が少し変わった

ソルバーの許容誤差、パッケージのバージョン、ハードウェア差によって、小さな数値差が生じることがあります。

## Git ブランチの混乱

現在のブランチとローカル変更を確認します。

```bash
git branch --show-current
git status
```

新しい機能を始める前に `main` に戻り、最新を pull してください。

```bash
git switch main
git pull origin main
```
