#!/usr/bin/python3
""" Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number, rounding up to 2 decimal places.

    Args:
        matrix: A list of integers or floats representing the matrix.
        div: The number to divide each element by.

    Raises:
        TypeError: If matrix is not a list of integers or floats, if the rows
        of the matrix have different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.
    
    Returns:
        A new matrix with the same dimensions as the input matrix, where each element
        has been divided by div and rounded to 2 decimal places.

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matr = [[round(elem / div, 2) for elem in row] for row in matrix]
    return matr