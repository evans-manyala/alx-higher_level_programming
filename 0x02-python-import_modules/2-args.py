#!/usr/bin/python3

def print_args():
    import sys
    num_of_args = len(sys.argv) - 1

    if num_of_args == 0:
        print("0 arguments.")
    elif num_of_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_of_args))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    print_args()
