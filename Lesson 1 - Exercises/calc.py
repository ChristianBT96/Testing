
# Calculator functions

# addition
def sum(number1, number2):
    return number1 + number2

# subtraction
def subtract(number1, number2):
    return number1 - number2

# multiplication
def multiply(number1, number2):
    return number1 * number2

# division with error handling for division by zero
def divide(number1, number2):
    if number2 == 0:
        raise ValueError("Cannot divide by zero.")
    return number1 / number2

