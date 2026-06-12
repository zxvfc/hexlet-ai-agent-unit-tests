"""Tests for the calculator module.

NOTE: Only add, subtract, and multiply are covered below.
The divide, factorial, and is_prime functions are NOT tested yet.
The AI agent should detect these gaps and write tests for them.
"""

import pytest
from src.calculator import add, subtract, multiply


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
