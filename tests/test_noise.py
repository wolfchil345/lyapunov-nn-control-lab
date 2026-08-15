import numpy as np
import pytest

from lyapunov_nn_control_lab.experimental_seeds import ExperimentSeedPlan
from lyapunov_nn_control_lab.noise import (
    add_measurement_noise,
    aggregate_noise_results,
    generate_standardized_measurement_noise,
    make_noisy_measurement_controller,
    run_measurement_noise_trials,
    save_noise_aggregate_csv,
    save_noise_trial_results_csv,
    scale_standardized_measurement_noise,
    simulate_with_measurement_noise,
)
from lyapunov_nn_control_lab.plotting import (
    save_noise_robustness_statistics_plot,
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


def test_common_random_noise_is_proportional_across_nonzero_levels():
    standardized = generate_standardized_measurement_noise(17, 8)
    low = scale_standardized_measurement_noise(standardized, 0.05)
    high = scale_standardized_measurement_noise(standardized, 0.2)

    assert np.allclose(high, (0.2 / 0.05) * low)


def test_simulation_exposes_matched_noise_and_exact_zero_condition():
    controller = lambda state: float(-state[0])
    zero = simulate_with_measurement_noise(
        controller,
        np.array([1.0, 0.0]),
        noise_std=0.0,
        seed=19,
        duration=0.03,
        dt=0.01,
    )
    low = simulate_with_measurement_noise(
        controller,
        np.array([1.0, 0.0]),
        noise_std=0.05,
        seed=19,
        duration=0.03,
        dt=0.01,
    )
    high = simulate_with_measurement_noise(
        controller,
        np.array([1.0, 0.0]),
        noise_std=0.2,
        seed=19,
        duration=0.03,
        dt=0.01,
    )

    assert np.array_equal(zero.measurement_noise, np.zeros((4, 2)))
    assert np.array_equal(
        low.standardized_measurement_noise,
        high.standardized_measurement_noise,
    )
    assert np.allclose(high.measurement_noise, 4.0 * low.measurement_noise)


def test_noise_trial_pairing_and_level_order_independence():
    controller = lambda state: float(-state[0])
    plan = ExperimentSeedPlan.explicit([23, 24])
    forward_rows, forward_solutions = run_measurement_noise_trials(
        controller,
        np.array([1.0, 0.0]),
        [0.0, 0.1],
        seed_plan=plan,
        duration=0.03,
        dt=0.01,
    )
    reverse_rows, reverse_solutions = run_measurement_noise_trials(
        controller,
        np.array([1.0, 0.0]),
        [0.1, 0.0],
        seed_plan=plan,
        duration=0.03,
        dt=0.01,
    )

    assert {
        level: {int(row["seed"]) for row in forward_rows if row["noise_std"] == level}
        for level in [0.0, 0.1]
    } == {0.0: {23, 24}, 0.1: {23, 24}}
    for pair in forward_solutions:
        assert np.array_equal(
            forward_solutions[pair].standardized_measurement_noise,
            reverse_solutions[pair].standardized_measurement_noise,
        )
        assert np.array_equal(
            forward_solutions[pair].measurement_noise,
            reverse_solutions[pair].measurement_noise,
        )


def test_noise_raw_and_aggregate_schemas(tmp_path):
    rows, _solutions = run_measurement_noise_trials(
        lambda state: float(-state[0]),
        np.array([1.0, 0.0]),
        [0.0, 0.1],
        seed_plan=ExperimentSeedPlan.explicit([31, 32]),
        duration=0.03,
        dt=0.01,
    )
    aggregates = aggregate_noise_results(rows)
    raw_path = tmp_path / "noise_trials.csv"
    aggregate_path = tmp_path / "noise_aggregates.csv"

    save_noise_trial_results_csv(rows, raw_path)
    save_noise_aggregate_csv(aggregates, aggregate_path)

    assert b"\r\n" not in raw_path.read_bytes()
    assert b"\r\n" not in aggregate_path.read_bytes()
    raw_header = raw_path.read_text(encoding="utf-8").splitlines()[0]
    aggregate_header = aggregate_path.read_text(encoding="utf-8").splitlines()[0]
    assert "noise_std" in raw_header
    assert "seed" in raw_header
    assert "common random-number realizations across noise amplitudes" in (
        raw_path.read_text(encoding="utf-8")
    )
    assert "final_state_norm_mean" in aggregate_header
    assert "final_state_norm_sample_std" in aggregate_header
    assert "final_state_norm_standard_error" in aggregate_header
    assert [row["n"] for row in aggregates] == [2, 2]

    save_noise_robustness_statistics_plot(rows, aggregates, tmp_path)
    assert (tmp_path / "noise_robustness_paired.png").exists()
