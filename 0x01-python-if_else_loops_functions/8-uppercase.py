#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if letter >= 'a' and letter <= 'z':
            chr(ord(letter) - (ord('a') - ord('A')))
        print("{}".format(letter), end='')
    print()
