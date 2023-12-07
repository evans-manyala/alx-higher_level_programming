#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for key, unique_value in list(new_dict.items()):
        if unique_value == value:
            del new_dict[key]
    return new_dict
