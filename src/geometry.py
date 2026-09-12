"""Geometry module providing simple shape area and perimeter calculations.

These functions are deliberately simple and easily testable,
making them ideal for demonstrating AI-agent unit test generation.
"""

import math


def circle_area(radius: float) -> float:
    """Return the area of a circle with the given radius.

    Area = π * r²

    Args:
        radius: The radius of the circle (must be non-negative).

    Returns:
        The area of the circle.

    Raises:
        ValueError: If radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius


def circle_circumference(radius: float) -> float:
    """Return the circumference of a circle with the given radius.

    Circumference = 2 * π * r

    Args:
        radius: The radius of the circle (must be non-negative).

    Returns:
        The circumference of the circle.

    Raises:
        ValueError: If radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius


def rectangle_area(width: float, height: float) -> float:
    """Return the area of a rectangle.

    Area = width * height

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        The area of the rectangle.

    Raises:
        ValueError: If width or height is negative.
    """
    if width < 0:
        raise ValueError("Width cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return width * height


def rectangle_perimeter(width: float, height: float) -> float:
    """Return the perimeter of a rectangle.

    Perimeter = 2 * (width + height)

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        The perimeter of the rectangle.

    Raises:
        ValueError: If width or height is negative.
    """
    if width < 0:
        raise ValueError("Width cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return 2 * (width + height)


def triangle_area(base: float, height: float) -> float:
    """Return the area of a triangle.

    Area = (base * height) / 2

    Args:
        base: The base length of the triangle.
        height: The height of the triangle.

    Returns:
        The area of the triangle.

    Raises:
        ValueError: If base or height is negative.
    """
    if base < 0:
        raise ValueError("Base cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return (base * height) / 2
