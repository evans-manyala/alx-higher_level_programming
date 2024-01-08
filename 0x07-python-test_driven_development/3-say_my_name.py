#!/usr/bin/python3
""" Function prints my first and last name"""


def say_my_name(first_name, last_name):
    """Function prints"""
    if not type(first_name) is str:
        raise TypeError ("First name must be string")
    elif not type(last_name) is str:
        raise TypeError("Last name is must be string")
    print(f"My name is {first_name}{last_name}")
