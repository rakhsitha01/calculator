"""
Simple Calculator
-----------------
- Accepts two numbers from the user.
- Performs addition, subtraction, multiplication and division.
- Handles division by zero without crashing.
"""

import math


def get_number(prompt):
    """Keep asking until the user types a valid, finite number."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("  Invalid input. Please enter a number (e.g. 12 or 3.5).")
            continue
        if not math.isfinite(value):
            print("  Please enter an ordinary number.")
            continue
        return value


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Return a / b, or None when b is zero."""
    if b == 0:
        return None
    return a / b


def fmt(value):
    """Show whole numbers without a trailing .0 and trim float noise."""
    if value.is_integer() and abs(value) < 1e15:
        return str(int(value))
    return f"{value:.10g}"


def main():
    print("=== Simple Calculator ===\n")
    while True:
        a = get_number("Enter first number : ")
        b = get_number("Enter second number: ")

        print("\nResults")
        print("-" * 34)
        print(f"{fmt(a)} + {fmt(b)} = {fmt(add(a, b))}")
        print(f"{fmt(a)} - {fmt(b)} = {fmt(subtract(a, b))}")
        print(f"{fmt(a)} * {fmt(b)} = {fmt(multiply(a, b))}")

        quotient = divide(a, b)
        if quotient is None:
            print(f"{fmt(a)} / {fmt(b)} = Error: cannot divide by zero")
        else:
            print(f"{fmt(a)} / {fmt(b)} = {fmt(quotient)}")
        print("-" * 34)

        again = input("\nCalculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram ended. Goodbye!")
