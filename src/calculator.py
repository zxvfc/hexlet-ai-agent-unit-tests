"""Calculator module providing basic arithmetic and number theory operations."""


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the quotient of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def factorial(n: int) -> int:
    """Return the factorial of n (n!).

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Check if n is a prime number.

    Args:
        n: An integer greater than 1.

    Returns:
        True if n is prime, False otherwise.

    Raises:
        ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("Prime numbers are defined for integers >= 2")
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b.

    Args:
        a: An integer.
        b: An integer.

    Returns:
        The GCD of a and b.

    Raises:
        ValueError: If a or b is negative.
    """
    if a < 0 or b < 0:
        raise ValueError("GCD is not defined for negative numbers")
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of a and b.

    Args:
        a: A non-negative integer.
        b: A non-negative integer.

    Returns:
        The LCM of a and b.

    Raises:
        ValueError: If a or b is negative.
    """
    if a < 0 or b < 0:
        raise ValueError("LCM is not defined for negative numbers")
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)
