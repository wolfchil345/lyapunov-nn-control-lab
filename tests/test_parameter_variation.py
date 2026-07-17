import numpy as np
import pytest

from src.parameter_variation import (
    make_state_space_matrices,
    simulate_parameter_variation,
)
from src.system import lqr_controller


def test_parameter_variation_matrix_shapes():
    a_matrix, b_matrix = make_state_space_matrices(
        mass=1.2,
        damping=0.4,
        stiffness=2.0,
    )

    assert a_matrix.shape == (2, 2)
    assert b_matrix.shape == (2, 1)


def test_parameter_variation_rejects_invalid_mass():
    with pytest.raises(ValueError):
        make_state_space_matrices(
            mass=0.0,
            damping=0.4,
            stiffness=2.0,
        )


def test_parameter_variation_rejects_negative_damping():
    with pytest.raises(ValueError):
        make_state_space_matrices(
            mass=1.0,
            damping=-0.1,
            stiffness=2.0,
        )


def test_lqr_converges_under_mild_parameter_variation():
    solution = simulate_parameter_variation(
        controller=lqr_controller,
        initial_state=np.array([1.5, 0.0]),
        mass=1.2,
        damping=0.3,
        stiffness=2.2,
    )

    final_norm = np.linalg.norm(solution.y[:, -1])

    assert solution.success
    assert final_norm < 1e-2
