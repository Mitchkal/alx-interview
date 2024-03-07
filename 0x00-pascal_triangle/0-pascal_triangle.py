#!/usr/bin/python3
"""
returns list of list of integers
representing pascal's triangle
"""


def pascal_triangle(n):
    """
    calculates row elements in triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # first row element is 1

        for k in range(1, row):
            new_row.append(prev_row[k - 1] + prev_row[k])

        new_row.append(1)  # last row element is 1
        triangle.append(new_row)
    return triangle
