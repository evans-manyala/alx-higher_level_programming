#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    # Addition
    print(f"{a} + {b} = {add(a, b)}")

    # Subtraction
    print(f"{a} - {b} = {sub(a, b)}")

    # Multiplication
    print(f"{a} * {b} = {mul(a, b)}")

    # Division
    print(f"{a} / {b} = {div(a, b)}")
