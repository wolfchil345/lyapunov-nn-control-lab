import subprocess
import sys


def test_quick_start_example_runs_successfully():
    result = subprocess.run(
        [sys.executable, "examples/quick_start.py"],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "Quick-start LQR simulation" in result.stdout
    assert "final_state_norm" in result.stdout
    assert "quadratic_cost" in result.stdout
