#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    newString = ""
    for c in str:
        if x != n:
            newString += c
        x += 1
    return newString
