#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_of_score = 0
    sum_of_weight = 0
    for score, weight in my_list:
        sum_of_score += score * weight
        sum_of_weight += weight

    if sum_of_weight == 0:
        return 0

    return sum_of_score / sum_of_weight
