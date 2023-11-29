#!/usr/bin/python3
def pow(a, b):
    if a == 0:
        return 0
    result = 1
    neg = False
    if a < 0:
        neg = True
        a = abs(a)
    for x in range(b):
        if neg:
            if b % 2 == 1:
                result *= -1
            neg = False
        result *= a
    return result
