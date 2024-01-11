#!/usr/bin/python3
"""Funciton creates the Pascal's triangle of n
rows as a list of lists of integers.
"""


def pascal_triangle(n):
    """
    Funciton creates the Pascal's triangle of n
    rows as a list of lists of integers.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list[list[int]]: A list of lists representing the Pascal's triangle.

    Raises:
        ValueError: If n is less than or equal to 0.
    """

    if n <= 0:
        raise ValueError("n must be a positive integer")

    triangle = [[1]]  # Initialize the first row

    # Generate remaining rows
    for _ in range(1, n):
        previous_row = triangle[-1]
        current_row = [previous_row[0]]
        for i in range(1, len(previous_row)):
            current_row.append(previous_row[i - 1] + previous_row[i])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
