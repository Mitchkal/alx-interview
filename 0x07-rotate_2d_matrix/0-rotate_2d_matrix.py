#!/usr/bin/python3
"""
module to rotate a 2 by 2 matrix
90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    rotates a 2d matrix 90 degrees
    clockwise
    """
    n = len(matrix)

    # Transposing
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reversing rows in transposed matrix
    for i in range(n):
        matrix[i].reverse()
