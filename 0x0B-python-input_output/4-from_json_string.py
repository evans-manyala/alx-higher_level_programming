#!/usr/bin/python3
"""
Function returns an object (Python data structure)
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
      my_str: A JSON string representing a Python object.

    Returns:
      Any: The Python object represented by the JSON string,
      or None if the string is not valid JSON.
    """
    return json.loads(my_str)
