import control as ct
import numpy as np

from src.validation import state_vector

MASS = 1.0
DAMPING = 0.4
STIFFNESS = 2.0

A = np.array(
    [
        [0.0, 1.0],
        [-STIFFNESS / MASS, -DAMPING / MASS],
    ],
    dtype=float,
)

B = np.array([[0.0], [1.0 / MASS]], dtype=float)

Q = np.diag([10.0, 1.0])
R = np.array([[0.5]])

K, P, CLOSED_LOOP_EIGENVALUES = ct.lqr(A, B, Q, R)
K = np.asarray(K, dtype=float)
P = np.asarray(P, dtype=float)


def lqr_controller(x: np.ndarray) -> float:
    """Return the LQR control input u = -Kx."""
    state = state_vector(x, name="x")
    return float((-K @ state.reshape(-1, 1)).item())
