#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx <= 0 or idx >= len(my_list):
                return my_list
    for x in range(idx + 1, len(my_list)):
            my_list[x - 1] = my_list[x]
    del my_list[-1]
    return my_list
