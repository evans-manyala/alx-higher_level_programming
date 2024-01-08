#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """This class inherits from list class"""
    def print_sorted(self):
        """Prints the list sorted in ascending order."""

        print(f"{', '.join(str(item) for item in sorted(self))}")
