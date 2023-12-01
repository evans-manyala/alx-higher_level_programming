#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0

    args = len(sys.argv) - 1

    if args == 0:
        print("{}".format(sum))
    else:
        for x in range(1, len(sys.argv)):
            sum += int(sys.argv[x])
        print("{}".format(sum))
