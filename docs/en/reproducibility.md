🌐 Language: [English](../en/reproducibility.md) | [日本語](../ja/reproducibility.md) | [한국어](../ko/reproducibility.md) | [ไทย](../th/reproducibility.md)

# Reproducibility

## Reproduce the checks

```bash
python -m pip install -e ".[dev]"
make checks
make quality-gate
```

## Reproduce the experiment

Back up tracked results, then run:

```bash
python scripts/run_full_experiment.py
```

The code seeds Python, NumPy, PyTorch, and available CUDA devices. Record the commit, Python version, dependency versions, device, and experiment settings with every result.

## Expected variation

Small numerical or PNG-encoding differences can occur across systems, devices, and library versions. Fixed seeds do not guarantee bit-for-bit identity across every CPU, GPU, BLAS implementation, or dependency release. Compare numeric metrics and, for figures, inspect pixel content before accepting changes.

## Scope

Reproducibility means the documented pipeline can recreate equivalent evidence. It does not turn sampled Lyapunov or region-of-attraction checks into a formal stability proof.
