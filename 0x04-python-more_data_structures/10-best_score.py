#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score_key, max_score_value = next(iter(a_dictionary.items()))
    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > max_score_value:
            max_score_key, max_score_value = key, value

    return max_score_key
