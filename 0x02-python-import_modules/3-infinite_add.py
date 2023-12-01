#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum, x = 0, 0
    for arg in sys.argv:
        if (x > 0):
            sum += int(arg)
        x += 1
        print(sum)
