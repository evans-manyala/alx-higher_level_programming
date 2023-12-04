#!usr/bin/python3
def divisible_by_2(my_list=[]):
    final_list = []
    for num in my_list:
        final_list.append(num % 2 == 0)
    return final_list
