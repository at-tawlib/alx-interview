#!/usr/bin/python3
"""Demo of Pascal's triangle"""


def pascal_triangle(n):
    """
    returns a list of Pasca's triangle based on n
    """
    triangle = []

    if n <= 0:
        return triangle
    for row in range(n):
        temp = []
        for j in range(row + 1):
            if j == 0 or j == row:
                temp.append(1)
            else:
                temp.append(triangle[row-1][j-1] + triangle[row-1][j])
        triangle.append(temp)

    return triangle
