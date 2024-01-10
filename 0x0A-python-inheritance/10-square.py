#!/usr/bin/python3
"""Class Rectangle that inherits fron Base Geometry class"""


Rectangle = __import__('9-rectangle.py')


class Square (Rectangle):
    """Represents a square, inheriting from the Rectangle class."""

    def __init__(self, size):
        """Initializes a square with a given size.

        Args:
            size (int): The length of a side of the square.

        Raises:
            ValueError: If size is not a positive integer.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Calculates and returns the area of the square."""

        return super().area()
