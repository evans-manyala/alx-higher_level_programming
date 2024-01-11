#!/usr/bin/python3
"""
Function adds all arguments to a Python list,
and then save them to a file
"""

import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_items_to_file():
    """
    Adds all command-line arguments to a Python list,
    loads any existing items from a file,combines the lists,
    and saves the result to a JSON file.
    """

    existing_items = load_from_json_file("add_item.json") or []

    new_items = sys.argv[1:]
    all_items = existing_items + new_items

    save_to_json_file(all_items, "add_item.json")
    print(f"Items saved to 'add_item.json': {all_items}")


if __name__ == "__main__":
    add_items_to_file()
