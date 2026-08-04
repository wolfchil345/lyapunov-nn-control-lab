import numpy as np

from src.system import CLOSED_LOOP_EIGENVALUES, A, B, K, P, Q, R


def test_mass_spring_damper_is_controllable():
    controllability_matrix = np.hstack((B, A @ B))

    assert np.linalg.matrix_rank(controllability_matrix) == A.shape[0]


def test_lqr_closed_loop_eigenvalues_are_stable():
    assert np.all(np.real(CLOSED_LOOP_EIGENVALUES) < 0.0)


def test_riccati_solution_is_symmetric_positive_definite():
    assert np.allclose(P, P.T, atol=1e-12)
    assert np.all(np.linalg.eigvalsh(P) > 0.0)


def test_lqr_solution_satisfies_continuous_riccati_equation():
    residual = A.T @ P + P @ A - P @ B @ np.linalg.solve(R, B.T @ P) + Q

    assert np.allclose(residual, np.zeros_like(residual), atol=1e-10)


def test_closed_loop_lyapunov_identity_matches_lqr_cost():
    closed_loop = A - B @ K
    derivative_matrix = closed_loop.T @ P + P @ closed_loop
    cost_matrix = Q + K.T @ R @ K

    assert np.allclose(derivative_matrix, -cost_matrix, atol=1e-10)
