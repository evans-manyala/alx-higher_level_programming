#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = set()
    sum_of_unique_values = 0

    for element in my_list:
        if isinstance(element, int):
            unique_values.add(element)

    for value in unique_values:
        sum_of_unique_values += value

    return sum_of_unique_values
