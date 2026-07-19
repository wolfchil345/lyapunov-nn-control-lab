# Experiment Log Template

Use this template to record important experiment runs and make result comparisons easier.

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
- Region-of-attraction output:

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

Do not describe sampled Lyapunov grid results as a complete formal proof of global stability.
