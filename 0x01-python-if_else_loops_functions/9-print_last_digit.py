#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        print("Number is 0")
    elif number < 10:
        print(number)
    else:
        last_digit = number % 10
        print(last_digit)
