#!/usr/bin/python3
"""rotate 2d matrix Module"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix function"""

    a = [list(row) for row in zip(*matrix)]
    b = [row[::-1] for row in a]
    cc = matrix.copy()
    for r in range(len(cc)):
        for c in range(len(cc[r])):
            matrix[r][c] = b[r][c]
