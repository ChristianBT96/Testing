
import pytest
from calc import sum, subtract, multiply, divide

def test_sum():
    assert sum(3, 5) == 8
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0
    # Test for decimal addition
    assert sum(2.5, 2.5) == 5.0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, -1) == 0
    assert subtract(0, 5) == -5
    # Test for decimal subtraction
    assert subtract(5.5, 2.5) == 3.0

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6
    # Test for decimal multiplication
    assert multiply(2.5, 4) == 10.0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(10, 0)

if __name__ == "__main__":
    pytest.main()
# Test cases for calculator functions
# To run the tests, use the command: pytest calc_tests.py
