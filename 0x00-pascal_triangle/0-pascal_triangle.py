#!/usr/bin/python3
"""
A function that prints Pascal's triangle
"""


def pascal_triangle(n):
    """Creates the triangle"""
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # First element of each row is always 1

        # Calculate the elements in between
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
