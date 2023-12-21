#!/usr/bin/python3
"""Defines class"""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square object with the given size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square (x, y). Defaults to (0, 0).
        """
        self._size = size
        self.position = position  # Set position using the property setter

    @property
    def size(self):
        """Get the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value
