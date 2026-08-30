🌐 언어: [English](../en/experiment_log_template.md) | [日本語](../ja/experiment_log_template.md) | [한국어](../ko/experiment_log_template.md) | [ไทย](../th/experiment_log_template.md)

# Experiment Log Template

이 template은 중요한 experiment runs를 기록하고 result comparisons를 더 쉽게 하기 위해 사용합니다.

## Basic information

- Date:
- Branch:
- Commit SHA:
- Research question:
- Experiment purpose:

## Environment

- Python version:
- PyTorch version:
- Device or runtime:
- Codespaces, VS Code, or local machine:

## Main settings

- Random seed:
- Number of epochs:
- Learning rate:
- Dataset size:
- Network architecture:
- Controller saturation limit:
- Initial condition:
- Simulation time:
- Lyapunov grid range:
- Lyapunov grid density:
- Noise setting:
- Parameter variation setting:

## Commands used

```bash
python scripts/check_environment.py
make checks
python main.py
python scripts/summarize_results.py
```

## Result files

- Metrics file:
- Summary report:
- Main trajectory plot:
- Control signal plot:
- Lyapunov plot or table:
- Robustness output:
- Finite-horizon convergence output:
- Horizon and final-state tolerance:
- State bounds, grid resolution, tested count, and converged count:

## Observations

- What improved?
- What became worse?
- Did the neural network controller behave close to LQR?
- Did Lyapunov-style checks show concerning states?
- Did robustness tests reveal failures?

## Comparison notes

- Compared against:
- Main difference from previous run:
- Is this comparison fair?
- Which parameter group changed?

## Conclusion

- Keep this result?
- Use in report or presentation?
- Need rerun?
- Next experiment idea:

## Safety note

sampled Lyapunov grid results를 global stability의 complete formal proof로 설명하지 마세요.

## Create a new log file

이 template의 timestamped copy를 만들려면 helper script를 사용하세요:

```bash
python scripts/new_experiment_log.py "baseline seed 0"
```

또는 Makefile shortcut을 사용하세요:

```bash
make new-log
```
