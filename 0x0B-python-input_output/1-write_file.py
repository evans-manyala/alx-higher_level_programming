#!/usr/bin/python3
"""
Writes a string to a text file (UTF-8) and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and
    returns the number of characters written.

    Args:
      filename (str, optional): The name of the file to write to.
      Defaults to "".text (str, optional):
      The string to write to the file. Defaults to "".

    Returns:
      int: The number of characters written to the file.
    """

    num_of_chars = 0
    with open(filename, "w", encoding="utf-8") as file:
        num_of_chars = len(text)
        file.write(text)
    return num_of_chars
