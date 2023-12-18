#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_items = 0
    try:
        for y in range(x):
            if isinstance(my_list[y], int):
                print("{:d}".format(my_list[y]), end="")
                printed_items += 1
    except (ValueError, TypeError):
        pass
    print()
    return printed_items
