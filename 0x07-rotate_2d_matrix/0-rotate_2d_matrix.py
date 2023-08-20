#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """
    Rotates a given square 2D matrix 90° clockwise in-place.
    Args:
        matrix (list of lists): The input square 2D matrix.
    Returns:
        None. The matrix is rotated in-place.
    """
    if not matrix:
        raise ValueError("Input matrix is empty.")

    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        raise ValueError("Input matrix is not square.")

    left, right = 0, cols - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            topLeft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1
