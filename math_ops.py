"""Small math utilities with a tiny self-test."""

def add(a, b):
    """Return a + b"""
    return a + b


def subtract(a, b):
    """Return a - b"""
    return a - b


def multiply(a, b):
    """Return a * b"""
    return a * b


def divide(a, b):
    """Return a / b (raises ZeroDivisionError if b == 0)"""
    return a / b


if __name__ == "__main__":
    print("add(2,3)", add(2, 3))
    print("subtract(5,2)", subtract(5, 2))
    print("multiply(4,3)", multiply(4, 3))
    try:
        print("divide(10,2)", divide(10, 2))
    except Exception as e:
        print("divide error:", e)
