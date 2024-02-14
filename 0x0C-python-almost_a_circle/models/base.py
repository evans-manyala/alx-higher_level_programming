#!/usr/bin/python3
"""Clas Base"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance.update(**dictionary)
