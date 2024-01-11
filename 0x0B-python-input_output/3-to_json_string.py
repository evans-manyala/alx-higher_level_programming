#!/usr/bin/python3
"""Function returns the JSON representation of an object string"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
      my_obj: Any object that can be serialized to JSON.

    Returns:
      str: The JSON representation of the object as a string.
    """

    try:
        json_string = json.dumps(my_obj)
    except TypeError:
        # Object cannot be serialized to JSON
        json_string = None
    return json_string
