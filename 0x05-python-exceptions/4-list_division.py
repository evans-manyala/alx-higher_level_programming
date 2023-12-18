#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for x in range(min(len(my_list_1), len(my_list_2), list_length)):
            try:
                if isinstance(my_list_1[x], (int, float)) and isinstance(
                    my_list_2[x], (int, float)
                ):
                    result = my_list_1[x] / my_list_2[x]
                else:
                    print("wrong type")
                    result = 0
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            result_list.append(result)
    except IndexError:
        print("out of range")
    if len(result_list) < list_length:
        result_list += [0] * (list_length - len(result_list))

    return result_list
