
ROMAN_VALUES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

VALID_SUBTRACTIVES = {
    ('I', 'V'), ('I', 'X'),
    ('X', 'L'), ('X', 'C'),
    ('C', 'D'), ('C', 'M')
}

def roman_to_decimal(roman: str) -> int:
    if not roman:
        raise ValueError("Empty string is not a valid Roman numeral.")

    total = 0
    prev_value = 0
    repeat_count = 0
    last_char = ''

    for i, char in enumerate(reversed(roman.upper())):
        if char not in ROMAN_VALUES:
            raise ValueError(f"Invalid Roman numeral character: {char}")

        value = ROMAN_VALUES[char]

        # Repetition rules
        if char == last_char:
            repeat_count += 1
            if char in ('V', 'L', 'D'):
                raise ValueError(f"Character {char} cannot be repeated.")
            if repeat_count > 2:
                raise ValueError(f"Character {char} repeated more than 3 times.")
        else:
            repeat_count = 0
        last_char = char

        # Subtractive notation
        if value < prev_value:
            if (char, roman[len(roman) - i - 2]) not in VALID_SUBTRACTIVES:
                raise ValueError(f"Invalid subtractive notation: {char}{roman[len(roman) - i - 2]}")
            total -= value
        else:
            total += value
            prev_value = value

    if total > 3999:
        raise ValueError("Roman numerals cannot represent numbers larger than 3999.")
    
    return total
