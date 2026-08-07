import numpy as np
import control as ct

from ._validation import validate_state

# The familiar mechanical names below denote coefficients in the normalized,
# dimensionless model m q'' + c q' + k q = u. They are not SI measurements.
SYSTEM_PARAMETER_CONVENTION = "normalized dimensionless model coefficients"
LQR_COST_CONVENTION = (
    "dimensionless weighted objective integrated over normalized time"
)

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
    state = validate_state(x, name="controller state")
    return float((-K @ state.reshape(2, 1)).item())
