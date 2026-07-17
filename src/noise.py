from collections.abc import Callable
from types import SimpleNamespace

import numpy as np

from src.system import A, B


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


def simulate_with_measurement_noise(
    controller: Callable[[np.ndarray], float],
    initial_state: np.ndarray,
    noise_std: float,
    seed: int = 7,
    duration: float = 10.0,
    dt: float = 0.01,
):
    """Simulate closed-loop dynamics with noisy state measurements."""

    if noise_std < 0.0:
        raise ValueError("Noise standard deviation must be nonnegative.")

    rng = np.random.default_rng(seed)

    time = np.arange(0.0, duration + dt, dt)
    states = np.zeros((2, len(time)), dtype=float)
    states[:, 0] = initial_state

    for index in range(len(time) - 1):
        true_state = states[:, index]

        measured_state = add_measurement_noise(
            true_state,
            noise_std,
            rng,
        )

        control = controller(measured_state)
        state_dot = A @ true_state + B[:, 0] * control

        states[:, index + 1] = true_state + dt * state_dot

        if not np.all(np.isfinite(states[:, index + 1])):
            return SimpleNamespace(
                t=time[: index + 2],
                y=states[:, : index + 2],
                success=False,
                message="Non-finite state encountered.",
            )

    return SimpleNamespace(
        t=time,
        y=states,
        success=True,
        message="Simulation completed successfully.",
    )
