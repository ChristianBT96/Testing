
import pytest
from roman_numerals import roman_to_decimal

@pytest.mark.parametrize("roman, expected", [
    ("I", 1),
    ("III", 3),
    ("IV", 4),
    ("IX", 9),
    ("XIII", 13),
    ("XL", 40),
    ("XC", 90),
    ("XCIV", 94),
    ("C", 100),
    ("CD", 400),
    ("D", 500),
    ("CM", 900),
    ("M", 1000),
    ("MCMXCIV", 1994),
    ("MMMCMXCIX", 3999),  # max value
])
def test_valid_roman_numerals(roman, expected):
    assert roman_to_decimal(roman) == expected

@pytest.mark.parametrize("roman", [
    "IIII",     # I repeated more than 3 times
    "VV",       # V repeated
    "LL",       # L repeated
    "DD",       # D repeated
    "IC",       # Invalid subtraction
    "XM",       # Invalid subtraction
    "IL",       # Invalid subtraction
    "VX",       # Invalid order
    #"MCMXCIVX", # Trailing invalid character
    "MMMM",     # Value exceeds 3999
    "ABC",      # Invalid characters
    "",         # Empty string
])
def test_invalid_roman_numerals(roman):
    with pytest.raises(ValueError):
        roman_to_decimal(roman)
