import numpy as np
import pytest

from lyapunov_nn_control_lab.noise import (
    add_measurement_noise,
    make_noisy_measurement_controller,
    simulate_with_measurement_noise,
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


@pytest.mark.parametrize("noise_std", [-0.1, np.nan, np.inf])
def test_noise_simulation_rejects_invalid_noise_std(noise_std):
    with pytest.raises(ValueError, match="noise standard deviation"):
        simulate_with_measurement_noise(
            lambda _state: 0.0,
            np.array([1.0, 0.0]),
            noise_std=noise_std,
        )


@pytest.mark.parametrize("dt", [0.0, -0.1, np.nan, np.inf])
def test_noise_simulation_rejects_invalid_dt(dt):
    with pytest.raises(ValueError, match="dt"):
        simulate_with_measurement_noise(
            lambda _state: 0.0,
            np.array([1.0, 0.0]),
            noise_std=0.0,
            dt=dt,
        )


def test_noise_simulation_uses_short_final_step_without_overshoot():
    solution = simulate_with_measurement_noise(
        lambda _state: 0.0,
        np.array([1.0, 0.0]),
        noise_std=0.0,
        duration=1.0,
        dt=0.3,
    )

    assert np.allclose(solution.t, [0.0, 0.3, 0.6, 0.9, 1.0])
    assert solution.t[-1] == 1.0


def test_noise_simulation_handles_dt_greater_than_duration():
    solution = simulate_with_measurement_noise(
        lambda _state: 0.0,
        np.array([1.0, 0.0]),
        noise_std=0.0,
        duration=1.0,
        dt=2.0,
    )

    assert np.array_equal(solution.t, [0.0, 1.0])
