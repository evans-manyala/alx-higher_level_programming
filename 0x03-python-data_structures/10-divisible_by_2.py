#!usr/bin/python3
def divisible_by_2(my_list=[]):
    final_list = []
    for num in my_list:
        if num % 1 == 0:
            final_list.append("True")
        else:
            final_list.append("False")
    return final_list
