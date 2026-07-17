import numpy as np
import pytest

from src.controllers import (
    make_saturated_controller,
    saturate_control,
)


def test_saturate_control_clips_positive_value():
    assert saturate_control(10.0, limit=5.0) == 5.0


def test_saturate_control_clips_negative_value():
    assert saturate_control(-10.0, limit=5.0) == -5.0


def test_saturate_control_keeps_value_inside_limit():
    assert saturate_control(3.0, limit=5.0) == 3.0


def test_saturate_control_rejects_nonpositive_limit():
    with pytest.raises(ValueError):
        saturate_control(1.0, limit=0.0)


def test_make_saturated_controller_wraps_controller():
    def raw_controller(x: np.ndarray) -> float:
        return 100.0

    controller = make_saturated_controller(
        raw_controller,
        limit=5.0,
    )

    assert controller(np.array([1.0, 0.0])) == 5.0
