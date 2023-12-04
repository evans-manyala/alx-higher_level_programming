#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for integer in range(len(matrix[row]) - 1):
            print("{:d}".format(matrix[row][integer]), end=' ')
        if matrix[row]:
            print("{:d}".format(matrix[row][-1]))
        else:
            print()
