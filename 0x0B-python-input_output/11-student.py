#!/usr/bin/python3
"""
Represents a student with first name, last name, and age.
"""

class Student:
    """Defines a student object with first name,
    last name and age"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with the given attributes.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student if in attributes"""
        if attrs is not None:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student instance with json"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)