#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    large_value = my_list[0]
    for value in my_list[1:]:
        if value > large_value:
            large_value = value
    return large_value
