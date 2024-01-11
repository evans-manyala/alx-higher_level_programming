#!/usr/bin/python3
"""function that creates an Object from a 'JSON file'"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
      filename: The name of the JSON file to read.

    Returns:
      Any: The Python object represented by the JSON file, or
      None if the file doesn't exist or is invalid JSON.
    """
    with open(filename, "r", encoding="utf-8") as file:
        json_string = file.read()
        return json.loads(json_string)
