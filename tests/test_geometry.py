"""Tests for the geometry module."""

import math
import pytest
from src.geometry import (
    circle_area,
    circle_circumference,
    rectangle_area,
    rectangle_perimeter,
    triangle_area,
)


class TestCircleArea:
    def test_area_zero(self):
        assert circle_area(0) == 0

    def test_area_positive(self):
        assert circle_area(1) == pytest.approx(math.pi)

    def test_area_radius_two(self):
        assert circle_area(2) == pytest.approx(math.pi * 4)

    def test_area_negative_raises(self):
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            circle_area(-1)


class TestCircleCircumference:
    def test_circumference_zero(self):
        assert circle_circumference(0) == 0

    def test_circumference_positive(self):
        assert circle_circumference(1) == pytest.approx(2 * math.pi)

    def test_circumference_large(self):
        assert circle_circumference(10) == pytest.approx(20 * math.pi)

    def test_circumference_negative_raises(self):
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            circle_circumference(-5)


class TestRectangleArea:
    def test_area_positive(self):
        assert rectangle_area(3, 4) == 12

    def test_area_zero_width(self):
        assert rectangle_area(0, 5) == 0

    def test_area_zero_height(self):
        assert rectangle_area(5, 0) == 0

    def test_area_negative_width_raises(self):
        with pytest.raises(ValueError, match="Width cannot be negative"):
            rectangle_area(-1, 5)

    def test_area_negative_height_raises(self):
        with pytest.raises(ValueError, match="Height cannot be negative"):
            rectangle_area(5, -2)

    def test_area_float_values(self):
        assert rectangle_area(2.5, 4.0) == 10.0


class TestRectanglePerimeter:
    def test_perimeter_positive(self):
        assert rectangle_perimeter(3, 4) == 14

    def test_perimeter_zero(self):
        assert rectangle_perimeter(0, 0) == 0

    def test_perimeter_negative_width_raises(self):
        with pytest.raises(ValueError, match="Width cannot be negative"):
            rectangle_perimeter(-1, 5)

    def test_perimeter_negative_height_raises(self):
        with pytest.raises(ValueError, match="Height cannot be negative"):
            rectangle_perimeter(5, -2)

    def test_perimeter_float(self):
        assert rectangle_perimeter(2.5, 3.5) == 12.0


class TestTriangleArea:
    def test_area_positive(self):
        assert triangle_area(4, 3) == 6.0

    def test_area_zero_base(self):
        assert triangle_area(0, 5) == 0.0

    def test_area_zero_height(self):
        assert triangle_area(5, 0) == 0.0

    def test_area_negative_base_raises(self):
        with pytest.raises(ValueError, match="Base cannot be negative"):
            triangle_area(-1, 5)

    def test_area_negative_height_raises(self):
        with pytest.raises(ValueError, match="Height cannot be negative"):
            triangle_area(5, -2)

    def test_area_float(self):
        assert triangle_area(3.0, 2.5) == 3.75
