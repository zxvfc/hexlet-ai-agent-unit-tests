# Feature: Geometry Module

## Description
Add a new `geometry` module that provides utility functions for calculating
areas and perimeters of basic geometric shapes (circles, rectangles, triangles).

## Functions to implement

1. **circle_area** - Calculate the area of a circle given its radius.
2. **circle_circumference** - Calculate the circumference of a circle given its radius.
3. **rectangle_area** - Calculate the area of a rectangle given width and height.
4. **rectangle_perimeter** - Calculate the perimeter of a rectangle given width and height.
5. **triangle_area** - Calculate the area of a triangle given base and height.

## Acceptance criteria

- All functions raise `ValueError` for negative dimensions.
- Zero is accepted as a valid input (degenerate shapes).
- Results are returned as `float`.
- The module is importable and functions behave as documented.

## Status

- [x] Implementation complete (`src/geometry.py`)
- [ ] Unit tests need to be written
