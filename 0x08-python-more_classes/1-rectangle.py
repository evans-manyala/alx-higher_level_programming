#!/usr/bin/python3
"""Models a rectangle class"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.

        Args:
                width: width of rectangle
                height: height of rectangle
        """
        self._height = height
        self._width = width

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
                Value: The value of the height

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is < 0.
        """
        if type(value) is not int:
            raise TypeError("Height must be an integer")

        if value < 0:
            raise ValueError("Height must be >= 0")

        self._height = value

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Args:
            Value: The value of the width
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is < 0.
        """
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")

        self._width = value
