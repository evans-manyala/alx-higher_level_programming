#!/usr/bin/python3
"""Creating a class Rectangle that defines a rectangle object"""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.

        Args:
            width: Width of the rectangle.
            height: Height of the rectangle.
        """
        self.width = width  # property setter for validation
        self.height = height  # property setter for validation

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, the type and value validation."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, the type and value validation."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle, even dimensions as zero."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle using '#'."""
        if self.width == 0 or self.height == 0:
            return ""  # Empty string for zero dimensions
        return "\n".join("#" * self.width for x in range(self.height))

    def __repr__(self):
        """Returns a string representation for recreating the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when a rectangle instance is deleted."""
        print("Bye rectangle...")
