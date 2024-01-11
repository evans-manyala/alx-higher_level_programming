#!/usr/bin/pythonnn3
"""Function writes an object to a text file using JSON Notation"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
      my_obj: Any object that can be serialized to JSON.
      filename: The name of the file to write to.

    Returns:
      None
    """

    with open(filename, "w", encoding="utf-8") as file:
        json_string = json.dumps(my_obj)
        file.write(json_string)
