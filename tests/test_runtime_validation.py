from __future__ import annotations

import numpy as np
import pytest

from lyapunov_nn_control_lab._validation import (
    build_time_grid,
    validate_state,
)
from lyapunov_nn_control_lab.simulation import simulate


@pytest.mark.parametrize(
    "state",
    [
        [],
        [1.0],
        [1.0, 2.0, 3.0],
        np.eye(2),
    ],
)
def test_validate_state_rejects_malformed_shapes(state):
    with pytest.raises(ValueError, match="shape \\(2,\\)"):
        validate_state(state)


@pytest.mark.parametrize(
    "state",
    [
        "position,velocity",
        np.array([1.0, 2.0], dtype=object),
        np.array(["1", "2"]),
    ],
)
def test_validate_state_rejects_nonnumeric_values(state):
    with pytest.raises(TypeError, match="numeric"):
        validate_state(state)


@pytest.mark.parametrize(
    "state",
    [
        [np.nan, 0.0],
        [np.inf, 0.0],
        [-np.inf, 0.0],
    ],
)
def test_validate_state_rejects_nonfinite_values(state):
    with pytest.raises(ValueError, match="finite"):
        validate_state(state)


@pytest.mark.parametrize(
    ("duration", "dt", "expected"),
    [
        (1.0, 0.25, [0.0, 0.25, 0.5, 0.75, 1.0]),
        (1.0, 0.3, [0.0, 0.3, 0.6, 0.9, 1.0]),
        (1.0, 2.0, [0.0, 1.0]),
    ],
)
def test_build_time_grid_includes_exact_duration_without_overshoot(
    duration,
    dt,
    expected,
):
    time = build_time_grid(duration, dt)

    assert np.allclose(time, expected)
    assert time[0] == 0.0
    assert time[-1] == duration
    assert np.all(time <= duration)


@pytest.mark.parametrize("duration", [0.0, -1.0, np.nan, np.inf])
def test_build_time_grid_rejects_invalid_duration(duration):
    with pytest.raises(ValueError, match="duration"):
        build_time_grid(duration, 0.1)


@pytest.mark.parametrize("dt", [0.0, -0.1, np.nan, np.inf])
def test_build_time_grid_rejects_invalid_dt(dt):
    with pytest.raises(ValueError, match="dt"):
        build_time_grid(1.0, dt)


def test_build_time_grid_rejects_absurd_size():
    with pytest.raises(ValueError, match="too large"):
        build_time_grid(1.0, 1e-12)


def test_simulate_rejects_noncallable_controller():
    with pytest.raises(TypeError, match="controller must be callable"):
        simulate(None, np.array([1.0, 0.0]))


def test_simulate_rejects_malformed_controller_output():
    with pytest.raises(ValueError, match="controller output must be a scalar"):
        simulate(lambda _state: np.array([1.0]), np.array([1.0, 0.0]))


@pytest.mark.parametrize("output", [np.nan, np.inf, -np.inf])
def test_simulate_rejects_nonfinite_controller_output(output):
    with pytest.raises(ValueError, match="controller output must be finite"):
        simulate(lambda _state: output, np.array([1.0, 0.0]))


def test_simulate_rejects_nonfinite_initial_state():
    with pytest.raises(ValueError, match="initial state.*finite"):
        simulate(lambda _state: 0.0, np.array([np.nan, 0.0]))


@pytest.mark.parametrize("duration", [0.0, -1.0, np.nan, np.inf])
def test_simulate_rejects_invalid_duration(duration):
    with pytest.raises(ValueError, match="duration"):
        simulate(lambda _state: 0.0, np.array([1.0, 0.0]), duration=duration)


def test_simulate_keeps_existing_sample_count():
    solution = simulate(
        lambda _state: 0.0,
        np.array([1.0, 0.0]),
        duration=1.0,
    )

    assert solution.t.size == 1001
    assert solution.t[0] == 0.0
    assert solution.t[-1] == 1.0
