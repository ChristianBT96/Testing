
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

    roman = roman.upper()
    total = 0
    i = 0
    repeat_count = 0
    last_char = ''

    while i < len(roman):
        current_char = roman[i]
        if current_char not in ROMAN_VALUES:
            raise ValueError(f"Invalid Roman numeral character: {current_char}")
        current_value = ROMAN_VALUES[current_char]

        # Check repetition
        if current_char == last_char:
            repeat_count += 1
            if current_char in ('V', 'L', 'D'):
                raise ValueError(f"Character {current_char} cannot be repeated.")
            if repeat_count >= 3:
                raise ValueError(f"Character {current_char} repeated more than 3 times.")
        else:
            repeat_count = 0
        last_char = current_char

        # Look ahead for subtractive pair
        if i + 1 < len(roman):
            next_char = roman[i + 1]
            if next_char not in ROMAN_VALUES:
                raise ValueError(f"Invalid Roman numeral character: {next_char}")
            next_value = ROMAN_VALUES[next_char]
            if current_value < next_value:
                if (current_char, next_char) not in VALID_SUBTRACTIVES:
                    raise ValueError(f"Invalid subtractive notation: {current_char}{next_char}")
                total += next_value - current_value
                i += 2
                continue

        total += current_value
        i += 1

    if total > 3999:
        raise ValueError("Roman numerals cannot represent numbers larger than 3999.")

    return total
