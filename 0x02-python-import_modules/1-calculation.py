#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

# Addition
sum = add(a, b)
print("Addition of", a, "and", b, "is:", sum)

# Subtraction
diff = sub(a, b)
print("Difference between", a, "and", b, "is:", diff)

# Multiplication
prod = mul(a, b)
print("Product of", a, "and", b, "is:", prod)

# Division
division = div(a, b)
print("Division of", a, "and", b, "is:", division)
