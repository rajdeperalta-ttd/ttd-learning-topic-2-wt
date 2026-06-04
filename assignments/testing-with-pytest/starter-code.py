# Starter Code: Testing with pytest
# These functions are already written for you.
# Your job is to write tests for them in a new file called test_functions.py


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def is_even(n):
    """Returns True if n is even, False otherwise."""
    return n % 2 == 0


def divide(a, b):
    """Returns a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
