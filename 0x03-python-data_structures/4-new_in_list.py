#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx or idx >= len(my_list):
        new_list = []
        x = 0
        for number in my_list:
            if x != idx:
                new_list.append(number)
            else:
                new_list.append(element)
            x = x + 1
        return new_list
    return my_list
