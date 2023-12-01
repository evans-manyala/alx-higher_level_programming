#!/usr/bin/python3
import calculator_1
import sys

if len(sys.argv) != 4:
    print("Uknonw length", file=sys.stderr)
    sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator not in "+-*/":
        print("Unknown operator.", file=sys.stderr)
        sys.exit(1)
    ans = 0

    if operator == "+":
        ans = calculator_1.add(a, b)
    elif operator == "-":
        ans = calculator_1.subtract(a, b)
    elif operator == "*":
        ans = calculator_1.multiply(a, b)
    else:
        ans = calculator_1.divide(a, b)
print("{} {} {} = {}".format(a, operator, b, ans))
