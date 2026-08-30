🌐 言語: [English](../en/experiment_log_template.md) | [日本語](../ja/experiment_log_template.md) | [한국어](../ko/experiment_log_template.md) | [ไทย](../th/experiment_log_template.md)

# Experiment Log Template

この template は、重要な experiment runs を記録し、result comparisons を容易にするために使用します。

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

sampled Lyapunov grid results を global stability の complete formal proof として記述してはいけません。

## Create a new log file

この template の timestamped copy を作成するには helper script を使用します。

```bash
python scripts/new_experiment_log.py "baseline seed 0"
```

または Makefile shortcut を使用します。

```bash
make new-log
```
