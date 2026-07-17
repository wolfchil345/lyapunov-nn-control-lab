from collections.abc import Callable

import numpy as np


def add_measurement_noise(
    state: np.ndarray,
    noise_std: float,
    rng: np.random.Generator,
) -> np.ndarray:
    """Add Gaussian measurement noise to the measured state."""

    if noise_std < 0.0:
        raise ValueError("Noise standard deviation must be nonnegative.")

    noise = rng.normal(
        loc=0.0,
        scale=noise_std,
        size=state.shape,
    )

    return state + noise


def make_noisy_measurement_controller(
    controller: Callable[[np.ndarray], float],
    noise_std: float,
    seed: int = 7,
) -> Callable[[np.ndarray], float]:
    """Wrap a controller so it receives noisy state measurements."""

    rng = np.random.default_rng(seed)

    def noisy_controller(true_state: np.ndarray) -> float:
        measured_state = add_measurement_noise(
            true_state,
            noise_std,
            rng,
        )

        return controller(measured_state)

    return noisy_controller
