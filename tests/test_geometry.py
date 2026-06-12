"""Tests for the geometry module.

All functions in src/geometry.py are tested:
- circle_area
- circle_circumference
- rectangle_area
- rectangle_perimeter
- triangle_area
"""

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
    def test_circle_area_positive(self):
        result = circle_area(1)
        assert result == pytest.approx(math.pi)

    def test_circle_area_large(self):
        result = circle_area(10)
        assert result == pytest.approx(math.pi * 100)

    def test_circle_area_zero(self):
        result = circle_area(0)
        assert result == 0.0

    def test_circle_area_float(self):
        result = circle_area(2.5)
        expected = math.pi * 2.5 * 2.5
        assert result == pytest.approx(expected)

    def test_circle_area_negative(self):
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            circle_area(-1)

    def test_circle_area_negative_float(self):
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            circle_area(-0.5)


class TestCircleCircumference:
    def test_circumference_positive(self):
        result = circle_circumference(1)
        assert result == pytest.approx(2 * math.pi)

    def test_circumference_large(self):
        result = circle_circumference(10)
        assert result == pytest.approx(2 * math.pi * 10)

    def test_circumference_zero(self):
        result = circle_circumference(0)
        assert result == 0.0

    def test_circumference_float(self):
        result = circle_circumference(2.5)
        expected = 2 * math.pi * 2.5
        assert result == pytest.approx(expected)

    def test_circumference_negative(self):
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            circle_circumference(-1)

    def test_circumference_negative_float(self):
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            circle_circumference(-0.5)


class TestRectangleArea:
    def test_rectangle_area_positive(self):
        result = rectangle_area(3, 4)
        assert result == 12

    def test_rectangle_area_floats(self):
        result = rectangle_area(2.5, 4.2)
        assert result == pytest.approx(10.5)

    def test_rectangle_area_zero_width(self):
        result = rectangle_area(0, 5)
        assert result == 0.0

    def test_rectangle_area_zero_height(self):
        result = rectangle_area(5, 0)
        assert result == 0.0

    def test_rectangle_area_zero_both(self):
        result = rectangle_area(0, 0)
        assert result == 0.0

    def test_rectangle_area_negative_width(self):
        with pytest.raises(ValueError, match="Width cannot be negative"):
            rectangle_area(-1, 5)

    def test_rectangle_area_negative_height(self):
        with pytest.raises(ValueError, match="Height cannot be negative"):
            rectangle_area(5, -1)

    def test_rectangle_area_both_negative(self):
        with pytest.raises(ValueError, match="Width cannot be negative"):
            rectangle_area(-1, -2)


class TestRectanglePerimeter:
    def test_rectangle_perimeter_positive(self):
        result = rectangle_perimeter(3, 4)
        assert result == 14

    def test_rectangle_perimeter_floats(self):
        result = rectangle_perimeter(2.5, 4.5)
        assert result == pytest.approx(14.0)

    def test_rectangle_perimeter_zero_width(self):
        result = rectangle_perimeter(0, 5)
        assert result == 10.0

    def test_rectangle_perimeter_zero_height(self):
        result = rectangle_perimeter(5, 0)
        assert result == 10.0

    def test_rectangle_perimeter_zero_both(self):
        result = rectangle_perimeter(0, 0)
        assert result == 0.0

    def test_rectangle_perimeter_negative_width(self):
        with pytest.raises(ValueError, match="Width cannot be negative"):
            rectangle_perimeter(-1, 5)

    def test_rectangle_perimeter_negative_height(self):
        with pytest.raises(ValueError, match="Height cannot be negative"):
            rectangle_perimeter(5, -1)

    def test_rectangle_perimeter_both_negative(self):
        with pytest.raises(ValueError, match="Width cannot be negative"):
            rectangle_perimeter(-1, -2)


class TestTriangleArea:
    def test_triangle_area_positive(self):
        result = triangle_area(6, 4)
        assert result == 12.0

    def test_triangle_area_floats(self):
        result = triangle_area(3.0, 2.5)
        assert result == pytest.approx(3.75)

    def test_triangle_area_zero_base(self):
        result = triangle_area(0, 5)
        assert result == 0.0

    def test_triangle_area_zero_height(self):
        result = triangle_area(5, 0)
        assert result == 0.0

    def test_triangle_area_zero_both(self):
        result = triangle_area(0, 0)
        assert result == 0.0

    def test_triangle_area_negative_base(self):
        with pytest.raises(ValueError, match="Base cannot be negative"):
            triangle_area(-1, 5)

    def test_triangle_area_negative_height(self):
        with pytest.raises(ValueError, match="Height cannot be negative"):
            triangle_area(5, -1)

    def test_triangle_area_both_negative(self):
        with pytest.raises(ValueError, match="Base cannot be negative"):
            triangle_area(-1, -2)
