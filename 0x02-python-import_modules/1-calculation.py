#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    # Addition
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Subtraction
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Multiplication
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Division
    print("{} / {} = {}".format(a, b, div(a, b)))
