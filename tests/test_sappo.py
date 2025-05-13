# tests/test_sappo.py

from sappo_core import values

def test_greet_user_output(capsys):
    values.greet_user("Faizal")
    captured = capsys.readouterr()
    assert "Faizal" in captured.out
