#!/usr/bin/python3

"""Defines a subclass MyList that imherits from List."""


class MyList(list):
    """This class inherits from list class"""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
