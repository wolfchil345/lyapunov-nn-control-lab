import subprocess
import sys
import json
import math
import numpy as np


def test_system_matrices_and_invariants():
    from lyapunov_nn_control_lab import lyapunov, system

    # Exact equality for directly defined matrices
    A_expected = np.array([[0.0, 1.0], [-2.0, -0.4]], dtype=float)
    B_expected = np.array([[0.0], [1.0 / 1.0]], dtype=float)
    Q_expected = np.diag([10.0, 1.0])
    R_expected = np.array([[0.5]])

    assert np.array_equal(system.A, A_expected)
    assert np.array_equal(system.B, B_expected)
    assert np.array_equal(system.Q, Q_expected)
    assert np.array_equal(system.R, R_expected)

    # DEFAULT_DECAY_MARGIN exact value
    assert lyapunov.DEFAULT_DECAY_MARGIN == 0.05


def test_lqr_K_P_tolerances():
    from lyapunov_nn_control_lab import system

    K_expected = np.array([[2.898979485566353, 2.4209854609927888]])
    P_expected = np.array(
        [[6.509974951242312, 1.4494897427831765], [1.4494897427831765, 1.2104927304963944]]
    )

    assert np.allclose(system.K, K_expected, rtol=1e-12, atol=1e-12)
    assert np.allclose(system.P, P_expected, rtol=1e-12, atol=1e-12)


def test_quick_start_regression_values():
    result = subprocess.run([sys.executable, "examples/quick_start.py"], capture_output=True, text=True, check=True)
    out = result.stdout
    # Parse the printed values
    found = {}
    for line in out.splitlines():
        if ":" in line and any(k in line for k in ("final_state_norm", "settling_time_s", "quadratic_cost")):
            key, val = line.split(":", 1)
            found[key.strip()] = float(val.strip())

    assert math.isclose(found.get("final_state_norm"), 0.001941, rel_tol=0, abs_tol=1e-9)
    assert math.isclose(found.get("settling_time_s"), 3.25, rel_tol=0, abs_tol=1e-9)
    assert math.isclose(found.get("quadratic_cost"), 6.510042, rel_tol=0, abs_tol=1e-9)
