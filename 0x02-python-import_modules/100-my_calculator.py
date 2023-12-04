#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator == "+":
        ans = calculator_1.add(a, b)
    elif operator == "-":
        ans = calculator_1.subtract(a, b)
    elif operator == "*":
        ans = calculator_1.multiply(a, b)
    else:
        ans = calculator_1.divide(a, b)
    print("{} {} {} = {}".format(a, operator, b, ans))
