#!/usr/bin/python3
"""Class Rectangle that inherits fron Base Geometry class"""


Rectangle = __import__('9-rectangle').Rectangle


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
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""

        return self.__size ** 2

    def __str__(self):
        """Returns string representation of the object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
