#!/usr/bin/python3
"""
A function that prints Pascal's triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for row_num in range(n):
        current_row = [1] * (row_num + 1)
        for col_num in range(1, row_num):
            current_row[col_num] = triangle[row_num - 1][col_num - 1] + triangle[row_num - 1][col_num]
        triangle.append(current_row)
        print(current_row)

