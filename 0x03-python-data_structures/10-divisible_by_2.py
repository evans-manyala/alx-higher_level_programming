#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    final_list = []

    for num in range(len(my_list)):
        final_list.append(True if my_list[num] % 2 == 0 else False)

    return final_list
