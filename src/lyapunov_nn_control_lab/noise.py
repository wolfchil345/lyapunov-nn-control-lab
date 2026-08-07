from collections.abc import Callable
from types import SimpleNamespace

import numpy as np

from .system import A, B
from ._validation import (
    build_time_grid,
    evaluate_controller,
    validate_controller,
    validate_nonnegative_scalar,
    validate_seed,
    validate_state,
)


def add_measurement_noise(
    state: np.ndarray,
    noise_std: float,
    rng: np.random.Generator,
) -> np.ndarray:
    """Add Gaussian measurement noise to the measured state."""

    state = validate_state(state, name="state")
    noise_std = validate_nonnegative_scalar(
        noise_std,
        name="noise standard deviation",
    )
    if not isinstance(rng, np.random.Generator):
        raise TypeError("rng must be a numpy.random.Generator.")

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

    controller = validate_controller(controller)
    noise_std = validate_nonnegative_scalar(
        noise_std,
        name="noise standard deviation",
    )
    seed = validate_seed(seed)
    rng = np.random.default_rng(seed)

    def noisy_controller(true_state: np.ndarray) -> float:
        measured_state = add_measurement_noise(
            true_state,
            noise_std,
            rng,
        )

        return evaluate_controller(controller, measured_state)

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

    controller = validate_controller(controller)
    initial_state = validate_state(initial_state, name="initial state")
    noise_std = validate_nonnegative_scalar(
        noise_std,
        name="noise standard deviation",
    )
    seed = validate_seed(seed)
    rng = np.random.default_rng(seed)

    time = build_time_grid(duration, dt)
    states = np.zeros((2, len(time)), dtype=float)
    states[:, 0] = initial_state

    for index in range(len(time) - 1):
        true_state = states[:, index]

        measured_state = add_measurement_noise(
            true_state,
            noise_std,
            rng,
        )

        control = evaluate_controller(controller, measured_state)
        state_dot = A @ true_state + B[:, 0] * control

        step = time[index + 1] - time[index]
        states[:, index + 1] = true_state + step * state_dot

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
