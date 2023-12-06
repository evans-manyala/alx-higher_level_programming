#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    combined_diff = [*set_1.difference(set_2), *set_2.difference(set_1)]
    return combined_diff