from types import SimpleNamespace

import numpy as np

from src.plotting import save_phase_portrait_plot


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
