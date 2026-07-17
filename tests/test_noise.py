import numpy as np
import pytest

from src.noise import (
    add_measurement_noise,
    make_noisy_measurement_controller,
)


def test_zero_noise_returns_same_state():
    rng = np.random.default_rng(7)
    state = np.array([1.0, -2.0])

    noisy_state = add_measurement_noise(
        state,
        noise_std=0.0,
        rng=rng,
    )

    assert np.allclose(noisy_state, state)


def test_negative_noise_std_raises_error():
    rng = np.random.default_rng(7)
    state = np.array([1.0, 0.0])

    with pytest.raises(ValueError):
        add_measurement_noise(
            state,
            noise_std=-0.1,
            rng=rng,
        )


def test_noisy_controller_returns_float():
    def raw_controller(x: np.ndarray) -> float:
        return float(x[0] + x[1])

    controller = make_noisy_measurement_controller(
        raw_controller,
        noise_std=0.01,
        seed=7,
    )

    output = controller(np.array([1.0, 2.0]))

    assert isinstance(output, float)
