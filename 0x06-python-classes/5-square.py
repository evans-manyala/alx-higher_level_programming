#!/usr/bin/python3
"""Define the class"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square object with the given size (default 0).

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        self._size = size # Private attribute

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

    def area(self):
        """Calculate and return the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square representation using '#' characters."""
        if self.size == 0:
            print()  # Print an empty line for size 0
        else:
            for _ in range(self.size):
                print("#" * self.size)
