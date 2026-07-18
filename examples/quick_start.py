from pathlib import Path
import sys

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.metrics import calculate_metrics
from src.simulation import simulate
from src.system import lqr_controller


def main() -> None:
    """Run a minimal LQR simulation example."""

    initial_state = np.array([1.0, 0.0])
    solution = simulate(
        lqr_controller,
        initial_state,
        duration=5.0,
    )

    metrics = calculate_metrics(
        solution,
        lqr_controller,
    )

    print("Quick-start LQR simulation")
    print(f"initial_state: {initial_state.tolist()}")
    print(f"final_state_norm: {metrics['final_state_norm']:.6f}")
    print(f"settling_time_s: {metrics['settling_time_s']}")
    print(f"quadratic_cost: {metrics['quadratic_cost']:.6f}")


if __name__ == "__main__":
    main()
