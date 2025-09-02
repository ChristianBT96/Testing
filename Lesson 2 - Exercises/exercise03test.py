import pytest
from exercise03script import printer_cartridges_price_calculator

# positive testing
# valid test cases

@pytest.mark.parametrize("amount, expected", [
(5, 50),
(6, 60),
(50, 500),
(98, 980),
(99, 990),
(100, 800),
(101, 808),
(150, 1200)
])
def test_valid_printer_cartriges_price_calculator(amount, expected):
    assert printer_cartridges_price_calculator(amount) == expected

# negative testing
# invalid test cases

@pytest.mark.parametrize("amount", [
(0),
(1),
(2),
(3),
(4)
])
def test_invalid_printer_cartriges_price_calculator(amount):
    with pytest.raises(ValueError):
        printer_cartridges_price_calculator(amount)