#!/usr/bin/python3
def best_score(a_dictionary):
    max_score_key = None
    max_score_value = None
    for key, value in a_dictionary.items():
        if isinstance(value, int):
            if max_score_value is None or value > max_score_value:
                max_score_key = key
                max_score_value = value
    return max_score_key
