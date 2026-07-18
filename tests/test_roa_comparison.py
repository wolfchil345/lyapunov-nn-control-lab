import numpy as np

from src.plotting import save_region_of_attraction_comparison_plot


def test_save_region_of_attraction_comparison_plot_creates_file(tmp_path):
    positions = np.linspace(-1.0, 1.0, 3)
    velocities = np.linspace(-1.0, 1.0, 3)

    convergence_map = np.array(
        [
            [False, True, False],
            [True, True, True],
            [False, True, False],
        ],
    )

    final_norm_map = np.array(
        [
            [0.5, 0.1, 0.5],
            [0.1, 0.0, 0.1],
            [0.5, 0.1, 0.5],
        ],
    )

    comparison_results = {
        "LQR": (
            positions,
            velocities,
            convergence_map,
            final_norm_map,
        ),
        "Neural network": (
            positions,
            velocities,
            convergence_map,
            final_norm_map,
        ),
        "Saturated NN": (
            positions,
            velocities,
            convergence_map,
            final_norm_map,
        ),
    }

    save_region_of_attraction_comparison_plot(
        comparison_results,
        tmp_path,
    )

    assert (tmp_path / "region_of_attraction_comparison.png").exists()
