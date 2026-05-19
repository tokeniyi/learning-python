"""
Scientific Calculator (Categorized Menu)
----------------------------------------
Supports:
- Basic arithmetic: Addition, Subtraction, Multiplication, Division
- Modulus, Exponentiation (with OverflowError handling)
- Factorial (with error handling for large inputs)
- Square Root
- Logarithm (base 10)
- Natural Logarithm (ln)
- Trigonometric functions: Sine, Cosine, Tangent
- Exit option

Features:
- Uses a dictionary to map menu choices to operations
- Displays menu grouped into categories (Basic vs Scientific)
- Validates user choice before asking for numbers
- Handles division/modulus by zero
- Handles invalid numeric input
- Handles OverflowError for factorial and exponentiation
"""

import math

# === Basic Operations ===
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y
def modulus(x, y):
    if y == 0:
        raise ZeroDivisionError("Modulus by zero is not allowed.")
    return x % y
def exponent(x, y):
    try:
        return x ** y
    except OverflowError:
        raise OverflowError("Result too large for exponentiation.")

# === Scientific Operations ===
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    try:
        return math.factorial(n)
    except OverflowError:
        raise OverflowError("Number too large for factorial calculation.")

def square_root(x):
    if x < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return math.sqrt(x)

def logarithm(x):
    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers.")
    return math.log10(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Natural log is not defined for non-positive numbers.")
    return math.log(x)

def sine(x): return math.sin(math.radians(x))   # input in degrees
def cosine(x): return math.cos(math.radians(x)) # input in degrees
def tangent(x): return math.tan(math.radians(x))# input in degrees

# === Categorized Operations Dictionary ===
operations = {
    "Basic": {
        '1': ("Addition (+)", add),
        '2': ("Subtraction (-)", subtract),
        '3': ("Multiplication (*)", multiply),
        '4': ("Division (/)", divide),
        '5': ("Modulus (%)", modulus),
        '6': ("Exponentiation (^)", exponent),
    },
    "Scientific": {
        '7': ("Factorial (!)", factorial),
        '8': ("Square Root (√)", square_root),
        '9': ("Logarithm (log10)", logarithm),
        '10': ("Natural Logarithm (ln)", natural_log),
        '11': ("Sine (sin)", sine),
        '12': ("Cosine (cos)", cosine),
        '13': ("Tangent (tan)", tangent),
    },
    "System": {
        '14': ("Exit", None)
    }
}

def calculator():
    """
    Main calculator loop.
    Displays categorized menu, processes user input,
    and performs the selected mathematical operation.
    """
    while True:
        # Display menu grouped by category
        print("\n=== Scientific Calculator Menu ===")
        for category, ops in operations.items():
            print(f"\n-- {category} Operations --")
            for key, (name, _) in ops.items():
                print(f"{key}. {name}")

        choice = input("\nEnter your choice (1-14): ").strip()

        # Exit condition
        if choice == '14':
            print("Exiting calculator. Goodbye!")
            break

        # Validate choice across all categories
        valid_choices = {key for cat in operations.values() for key in cat.keys()}
        if choice not in valid_choices:
            print("Invalid choice. Please select from 1-14.")
            continue

        try:
            # Single-input operations
            if choice in ['7', '8', '9', '10', '11', '12', '13']:
                num = float(input("Enter a number: "))
                try:
                    result = None
                    if choice == '7':  # Factorial requires integer input
                        num = int(num)
                    result = [ops[choice][1](num) for ops in operations.values() if choice in ops][0]
                    print(f"Result: {result}")
                except (ValueError, OverflowError) as e:
                    print(f"Error: {e}")

            else:
                # Two-input operations
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                try:
                    result = [ops[choice][1](num1, num2) for ops in operations.values() if choice in ops][0]
                    print(f"Result: {result}")
                except ZeroDivisionError as zde:
                    print(f"Error: {zde}")
                except OverflowError as oe:
                    print(f"Error: {oe}")

        except ValueError:
            print("Invalid input. Please enter numeric values only.")

# Run the calculator
if __name__ == "__main__":
    calculator()
