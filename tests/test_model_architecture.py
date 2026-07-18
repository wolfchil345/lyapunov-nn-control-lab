from src.plotting import save_model_architecture_diagram


def test_save_model_architecture_diagram_creates_file(tmp_path):
    save_model_architecture_diagram(tmp_path)

    assert (tmp_path / "model_architecture.png").exists()
