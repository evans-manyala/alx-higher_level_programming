#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if letter.islower():
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end='')
    print()
