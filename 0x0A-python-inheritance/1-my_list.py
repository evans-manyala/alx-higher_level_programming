#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """This class inherits from list class"""

    def __init__(self):
        """initializing"""
        super().__init__()

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
