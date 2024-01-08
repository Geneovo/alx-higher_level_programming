#!/usr/bin/python3
"""This modules divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (list): List of lists of integers or floats
        div (int or float): Number to divide by

    Returns:
        list: New matrix with the result of the division

    Raises:
        TypeError: if the elements of the matrix are not lists
                   if the elements of the lists are not integer/floats
                   if div is not an integer/float number
                   if the lists of the matrix don't have the same size

        ZeroDivisionError: if div is equal to 0
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    message_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(message_type)

    len_gth = 0
    message_size = "Each row of th matrix must have the same size"

    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(message_type)

        if len_gth != 0 and len(row) != len_gth:
            raise TypeError(message_size)

        for element in row:
            if not type(element) in (int, float):
                raise TypeError(message_type)

            len_gth = len(row)

        new = list(
            map(
                lambda x: list(
                    map(lambda y: round(y / div, 2), x)), matrix))
        return (new)
