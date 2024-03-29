class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square object with the given size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square (x, y).
            Defaults to (0, 0).
        """
        self._size = size
        if position:  # Check if position is provided
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

    @property
    def position(self):
        """Get the current position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(x, int) and x > 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square representation using '#' characters."""
        if self.size == 0:
            print()  # Empty line for size 0
        else:
            for i in range(self.position[1]):
                print()  # Print empty lines for vertical position
            for _ in range(self.size):
                print(
                    " " * self.position[0], end=""
                )  # Print spaces for horizontal position
                print("#" * self.size)
