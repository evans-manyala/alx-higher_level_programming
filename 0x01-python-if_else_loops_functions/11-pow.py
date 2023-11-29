#!/usr/bin/python3
def pow(a, b):
    if a == 0:
        return 0
    result = 1
    neg = False
    if a < 0:
        neg = True
        a = abs(a)
    for x in range(abs(b)):
        result *= a
    if b < 0:
        result = 1 / result
    if neg:
        result *= -1
    return result
