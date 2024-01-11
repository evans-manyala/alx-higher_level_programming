#!/usr/bin/python3
"""Function appends text into a file"""


def append_write(filename="", text=""):
  """
  Appends a string to the end of a text file (UTF-8) and returns the number of characters added.

  Args:
    filename (str, optional): The name of the file to append to. Defaults to "".
    text (str, optional): The string to append to the file. Defaults to "".

  Returns:
    int: The number of characters added to the file.
  """

  append_chars = 0
  with open(filename, "a", encoding="utf-8") as file:
    append_chars = len(text)
    file.write(text)
  return append_chars
