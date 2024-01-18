#!/usr/bin/python3
"""Class Base"""


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
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                list = cls.from_json_string(file.read())
                return [cls.create(**dic) for dic in list]
        except FileNotFoundError:
            return []
