#!/usr/bin/python3
"""


"""


def class_to_json(obj):
    """
    Returns a dictionary description of an object
    suitable for JSON serialization.

    Returns:
        dict: A dictionary representing the object's data structure
        for JSON serialization.
    """

    def class_to_json(obj):
        """Returns the dictionary description of the object"""
    return obj.__dict__
