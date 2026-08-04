"""Random-seed configuration for repeatable experiments."""

from __future__ import annotations

import random

import numpy as np
import torch


def set_global_seed(seed: int, *, torch_threads: int = 1) -> None:
    """Seed Python, NumPy, and PyTorch, including available CUDA devices."""

    if isinstance(seed, bool) or not isinstance(seed, int):
        raise TypeError("seed must be an integer.")
    if torch_threads < 1:
        raise ValueError("torch_threads must be at least 1.")

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.set_num_threads(torch_threads)
