# Scientific Result Artifacts

The files stored directly in `results/` are legacy, unverified historical
artifacts. They remain useful records, but they predate the complete run-level
provenance system and some also predate corrected Lyapunov margin reporting,
finite-horizon convergence terminology, normalized-state labels, paired
stability-weight seeds, or common-random-number noise comparisons.

This classification does not mean the historical data are invalid. It means
their code, configuration, environment, seed, and checksum provenance is less
complete than the current pipeline can provide. The original tracked files are
preserved byte-for-byte and are not silently relabelled.

New runs are published under:

```text
results/runs/<run_id>/
├── manifest.json
├── SHA256SUMS
├── report.md
├── raw and aggregate CSV files
├── figures
└── model state
```

A run is complete only when `manifest.json` has `"status": "complete"` and
all recorded files pass checksum verification. Generate and verify runs with:

```bash
python main.py
python scripts/verify_run.py results/runs/<run_id>
python scripts/list_results.py
```

Official runs require a clean Git working tree. `--allow-dirty` permits an
explicitly exploratory run, and the manifest records `git_dirty: true`.
