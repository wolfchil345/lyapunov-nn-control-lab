from types import SimpleNamespace

import numpy as np

from src.plotting import save_lyapunov_contour_plot


def test_save_lyapunov_contour_plot_creates_file(tmp_path):
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

    lyapunov_matrix = np.eye(2)

    save_lyapunov_contour_plot(
        [solution],
        [np.array([1.0, 0.0])],
        lyapunov_matrix,
        tmp_path,
    )

    assert (tmp_path / "lyapunov_contours.png").exists()
