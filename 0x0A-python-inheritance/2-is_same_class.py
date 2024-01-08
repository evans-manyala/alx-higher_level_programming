#!/usr/bin/python3

"""The module has a function that returns True if the object is exactly an
instance of the specified class."""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly
    an instance of the specified class ; otherwise False
    """
    return type(obj) is a_class
