#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    make an n x n 2D matrix rotate 90 degrees clockwise
    """
    n = len(matrix)

    # first lets tranpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # then we reverse the matrix
    for row in matrix:
        row.reverse()

    return matrix
