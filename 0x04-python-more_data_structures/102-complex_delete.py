#!/usr/bin/python3
def complex_delete(a_dictionary, value):
  for key, unique_value in list(a_dictionary.items()):
    if unique_value == value:
       del a_dictionary[key]
