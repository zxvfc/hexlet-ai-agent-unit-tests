"""Tests for the calculator module.

NOTE: Only add, subtract, and multiply are covered below.
The divide, factorial, and is_prime functions are NOT tested yet.
The AI agent should detect these gaps and write tests for them.
"""

import pytest
from src.calculator import add, subtract, multiply, divide, factorial, is_prime


class TestAdd:
    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -2) == -3

    def test_add_zero(self):
        assert add(5, 0) == 5
        assert add(0, 0) == 0


class TestSubtract:
    def test_subtract_positive(self):
        assert subtract(10, 3) == 7

    def test_subtract_negative_result(self):
        assert subtract(3, 10) == -7

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5


class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negative(self):
        assert multiply(-3, 4) == -12
        assert multiply(-3, -4) == 12


class TestDivide:
    def test_divide_positive(self):
        assert divide(10, 2) == 5.0

    def test_divide_fraction(self):
        assert divide(1, 3) == pytest.approx(0.3333333)

    def test_divide_by_one(self):
        assert divide(7, 1) == 7.0

    def test_divide_zero_numerator(self):
        assert divide(0, 5) == 0.0

    def test_divide_negative(self):
        assert divide(-10, 2) == -5.0
        assert divide(10, -2) == -5.0

    def test_divide_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(5, 0)


class TestFactorial:
    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_small(self):
        assert factorial(5) == 120

    def test_factorial_large(self):
        assert factorial(10) == 3628800

    def test_factorial_negative_raises(self):
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)

    def test_factorial_negative_large_raises(self):
        with pytest.raises(ValueError):
            factorial(-100)


class TestIsPrime:
    def test_is_prime_two(self):
        assert is_prime(2) is True

    def test_is_prime_three(self):
        assert is_prime(3) is True

    def test_is_prime_large_prime(self):
        assert is_prime(17) is True
        assert is_prime(97) is True

    def test_is_prime_even_composite(self):
        assert is_prime(4) is False

    def test_is_prime_odd_composite(self):
        assert is_prime(9) is False
        assert is_prime(15) is False

    def test_is_prime_one_raises(self):
        with pytest.raises(ValueError, match="Prime numbers are defined for integers >= 2"):
            is_prime(1)

    def test_is_prime_zero_raises(self):
        with pytest.raises(ValueError):
            is_prime(0)

    def test_is_prime_negative_raises(self):
        with pytest.raises(ValueError):
            is_prime(-5)
