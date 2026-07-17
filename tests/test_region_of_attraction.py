from types import SimpleNamespace

import numpy as np
import pytest

from src.plotting import save_region_of_attraction_plot
from src.region_of_attraction import evaluate_region_of_attraction
from src.system import lqr_controller


def test_region_of_attraction_shapes():
    positions, velocities, convergence_map, final_norm_map = evaluate_region_of_attraction(
        lqr_controller,
        position_range=(-0.5, 0.5),
        velocity_range=(-0.5, 0.5),
        num_points=3,
        convergence_threshold=1.0,
        duration=1.0,
    )

    assert positions.shape == (3,)
    assert velocities.shape == (3,)
    assert convergence_map.shape == (3, 3)
    assert final_norm_map.shape == (3, 3)


def test_region_of_attraction_rejects_too_few_points():
    with pytest.raises(ValueError):
        evaluate_region_of_attraction(
            lqr_controller,
            num_points=1,
        )


def test_save_region_of_attraction_plot_creates_file(tmp_path):
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

    save_region_of_attraction_plot(
        positions,
        velocities,
        convergence_map,
        final_norm_map,
        tmp_path,
    )

    assert (tmp_path / "region_of_attraction.png").exists()
