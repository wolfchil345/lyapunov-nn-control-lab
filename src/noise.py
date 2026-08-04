from collections.abc import Callable
from types import SimpleNamespace

import numpy as np

from src.system import A, B
from src.validation import nonnegative_number, positive_number, state_vector


def add_measurement_noise(
    state: np.ndarray,
    noise_std: float,
    rng: np.random.Generator,
) -> np.ndarray:
    """Add Gaussian measurement noise to the measured state."""

    state = state_vector(state)
    noise_std = nonnegative_number(noise_std, name="noise_std")

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

    initial_state = state_vector(initial_state, name="initial_state")
    noise_std = nonnegative_number(noise_std, name="noise_std")
    duration = positive_number(duration, name="duration")
    dt = positive_number(dt, name="dt")

    rng = np.random.default_rng(seed)

    num_steps = int(np.ceil(duration / dt))
    time = np.linspace(0.0, duration, num_steps + 1)
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
        if not np.isfinite(control):
            return SimpleNamespace(
                t=time[: index + 1],
                y=states[:, : index + 1],
                success=False,
                message="Non-finite control input encountered.",
            )
        state_dot = A @ true_state + B[:, 0] * control

        step_size = time[index + 1] - time[index]
        states[:, index + 1] = true_state + step_size * state_dot

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
