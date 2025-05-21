# tests/test_core.py
from core.processor import start_ai

def test_start_ai():
    assert callable(start_ai)
