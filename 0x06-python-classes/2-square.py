#!/usr/bin/python3

"""
Define a class Square.
"""


class Square:
    def __init__(self, size=0):
        """
        Represents a square

        Args:
            size (int): the size of the square (default is 0)
        """
        # size must be an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # size should not be less than Zero
        if size < 0:
            raise ValueError("size must be >= 0")

        # calculate size of the Square if all goes well
        self.__size = size
