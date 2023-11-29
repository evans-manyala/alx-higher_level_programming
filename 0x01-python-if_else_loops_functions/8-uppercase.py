#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 'a' <= letter <= 'z':
            chr(ord(letter) - 32)
        print('{}'.format(letter), end='')
    print()
