#!/usr/bin/python3
"""


"""


def class_to_json(obj):
    """
    Returns a dictionary description of an object
    suitable for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes
        (list, dict, str, int, bool).

    Returns:
        dict: A dictionary representing the object's data structure
        for JSON serialization.
    """

    data = {}
    for attr in dir(obj):
        if not attr.startswith("_"):
            value = getattr(obj, attr)
            if isinstance(value, (list, dict, str, int, bool)):
                data[attr] = value
            elif isinstance(value, (tuple, set)):
                data[attr] = list(value)
            else:
                pass
    return data
