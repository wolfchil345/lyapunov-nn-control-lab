🌐 言語: [English](../en/result_review_checklist.md) | [日本語](../ja/result_review_checklist.md) | [한국어](../ko/result_review_checklist.md) | [ไทย](../th/result_review_checklist.md)

# Result Review Checklist

この checklist は、生成された result files を report、presentation、thesis chapter、portfolio で使う前に使用します。

## 1. 実験設定を確認する

- controller type が明確である
- random seed が記録されている
- number of epochs が記録されている
- Lyapunov grid size が記録されている
- finite-horizon convergence 結果に、horizon、strict final-state tolerance、bounds、resolution、tested count、converged count が記録されている
- noise または parameter variation の設定が記録されている

## 2. 生成ファイルを確認する

次を実行します。

```bash
python scripts/list_results.py
```

重要ファイルの名前が明確で、正しい実験と対応していることを確認します。

## 3. プロットをレビューする

- 安定が期待される場合、軌道が原点へ向かっている
- control signals に説明のない異常スパイクがない
- 比較プロットに LQR、neural network、他の制御器が明確にラベルされている
- 図が slides や reports で読める十分な可読性を持つ

## 4. metrics をレビューする

- metrics は互換設定の実験間でのみ比較する
- 低コストや低誤差だけを安定性の証明として扱わない
- control effort は tracking または stabilization quality と合わせて評価する

## 5. Lyapunov 関連出力をレビューする

- grid-based checks は sampled evidence として記述されている
- formal proof が実際にある場合を除き、global proof を主張していない
- 問題ケースを黙って無視せず、保持して説明している

## 6. finite-horizon convergence 出力をレビューする

- percentage が horizon、tolerance、sampled grid と一緒に報告されている
- finite-time pass を formal attraction region と呼んでいない
- finite-time failure を asymptotic divergence の証拠として扱っていない
- convergence map と sampled Lyapunov checks を概念的に分離している

## 7. robustness 出力をレビューする

- noise level または parameter variation が明確に記載されている
- failed cases が記録されている
- robustness results を baseline results とラベルなしで混在させていない

## 8. 結果を commit する前に

次を実行します。

```bash
python scripts/check_environment.py
make checks
python scripts/list_results.py
git status
```

result files の commit は、有用な例、最終 artifact、または文書化に必要なものだけにします。

## 最終ルール

重要な結果はすべて、file name、experiment log、関連ドキュメントから理解可能であるべきです。
