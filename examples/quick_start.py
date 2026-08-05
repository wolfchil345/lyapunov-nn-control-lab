import numpy as np

from lyapunov_nn_control_lab.metrics import calculate_metrics
from lyapunov_nn_control_lab.simulation import simulate
from lyapunov_nn_control_lab.system import lqr_controller


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
