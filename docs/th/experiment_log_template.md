🌐 ภาษา: [English](../en/experiment_log_template.md) | [日本語](../ja/experiment_log_template.md) | [한국어](../ko/experiment_log_template.md) | [ไทย](../th/experiment_log_template.md)

# Experiment Log Template

ใช้ template นี้เพื่อบันทึก experiment runs ที่สำคัญ และทำให้การเปรียบเทียบผลลัพธ์ทำได้ง่ายขึ้น

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

ห้ามอธิบาย sampled Lyapunov grid results ว่าเป็น complete formal proof ของ global stability

## Create a new log file

ใช้ helper script เพื่อสร้างสำเนาแบบ timestamped ของ template นี้:

```bash
python scripts/new_experiment_log.py "baseline seed 0"
```

หรือใช้ Makefile shortcut:

```bash
make new-log
```
