# tests/test_main.py
import pytest
from main import add_numbers, subtract_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(5, 2) == 3
    assert subtract_numbers(10, 10) == 0
    assert subtract_numbers(-1, -1) == 0