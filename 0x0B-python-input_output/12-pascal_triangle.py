#!/usr/bin/python3
"""Module that defines a funtion that generates Pascal's triangle"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the nth row
    Args:
        n (int): Size of triangle
    Returns:
        list of lists: Pascal's triangle represented as list of lists of int
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for x in range(1, n):
        size = [1]
        for y in range(1, x):
            size.append(triangle[x - 1][y - 1] + triangle[x - 1][y])
        size.append(1)
        triangle.append(size)

    return triangle
