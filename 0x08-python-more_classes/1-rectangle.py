#!/usr/bin/python3
"""
Define a class rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.
        """
        self._Rectangle__width = 0
        self._Rectangle__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        else:
            self._Rectangle__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be >= 0")
        else:
            self._Rectangle__height = value
