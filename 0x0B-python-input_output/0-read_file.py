#!usr/bin/python3
"""Function reads a file and prints to the stdout"""


def read_file(filename=""):
    """Reads the contents of a UTF-8 text file and prints it to stdout.

    Args:
        filename (str, optional): The name of the file to read. Defaults to "".
    """

    with open(filename, "r", encoding="utf-8") as file:
        file_content = file.read()
        print(file_content, end="")
