import subprocess
import os


def test_model_training():
    """Check that train.py runs without errors."""
    result = subprocess.run(["python", "train.py"], capture_output=True)
    assert result.returncode == 0, f"Training script failed!\n{result.stderr.decode()}"


def test_artifact_created():
    """Check that the model artifact was actually saved."""
    assert os.path.exists("artifacts/model.pkl"), "Model artifact not found!"


def test_evaluate_runs():
    """Check that evaluate.py runs without errors."""
    result = subprocess.run(["python", "evaluate.py"], capture_output=True)
    assert result.returncode == 0, f"Evaluate script failed!\n{result.stderr.decode()}"


def test_metrics_file_created():
    """Check that evaluate.py produced a metrics file."""
    assert os.path.exists("artifacts/metrics.txt"), "Metrics file not found!"