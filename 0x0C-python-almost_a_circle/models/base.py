#!/usr/bin/python3
"""Clas Base"""


class Base:
    __nb_objects = 0  # Private class attribute to count objects

    def __init__(self, id=None):
        """
        Initializes a new Base object.

        Args:
            id (int, optional): The ID of the object
            If not provided, a new ID is generated.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
