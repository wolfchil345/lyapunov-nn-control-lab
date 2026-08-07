from types import SimpleNamespace

import numpy as np
import pytest

from lyapunov_nn_control_lab.plotting import (
    save_finite_horizon_convergence_comparison_plot,
    save_model_architecture_diagram,
    save_phase_portrait_plot,
    save_saturation_comparison_plot,
)


def test_save_phase_portrait_plot_creates_file(tmp_path):
    time = np.linspace(0.0, 1.0, 5)

    solution = SimpleNamespace(
        t=time,
        y=np.array(
            [
                [1.0, 0.7, 0.4, 0.2, 0.0],
                [0.0, -0.2, -0.2, -0.1, 0.0],
            ],
        ),
    )

    save_phase_portrait_plot(
        [solution],
        [np.array([1.0, 0.0])],
        tmp_path,
    )

    assert (tmp_path / "phase_portrait.png").exists()


def test_plotting_rejects_mismatched_or_empty_required_collections(tmp_path):
    solution = SimpleNamespace(
        t=np.array([0.0, 1.0]),
        y=np.zeros((2, 2)),
    )

    with pytest.raises(ValueError, match="same length"):
        save_phase_portrait_plot(
            [solution],
            [np.array([1.0, 0.0]), np.array([0.0, 1.0])],
            tmp_path,
        )
    with pytest.raises(ValueError, match="must not be empty"):
        save_saturation_comparison_plot({}, tmp_path)
    with pytest.raises(ValueError, match="must not be empty"):
        save_finite_horizon_convergence_comparison_plot({}, tmp_path)


def test_plot_writer_creates_nested_output_directory(tmp_path):
    output_dir = tmp_path / "nested" / "figures"

    save_model_architecture_diagram(output_dir)

    assert (output_dir / "model_architecture.png").exists()
