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
