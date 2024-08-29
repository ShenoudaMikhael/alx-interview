#!/usr/bin/python3
from sys import argv


def is_queen(apatch: list) -> bool:
    """is_NQueen"""
    row_number = len(apatch) - 1
    difference = 0
    for index in range(0, row_number):
        difference = apatch[index] - apatch[row_number]
        if difference < 0:
            difference *= -1
        if difference == 0 or difference == row_number - index:
            return False
    return True


def solve(dimension: int, row: int, apatch: list, aresult: list):
    """solve function"""
    if row == dimension:
        print(aresult)
    else:
        for column in range(0, dimension):
            apatch.append(column)
            aresult.append([row, column])
            if is_queen(apatch):
                solve(dimension, row + 1, apatch, aresult)
            apatch.pop()
            aresult.pop()


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(argv[1])
except Exception:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)
else:
    result = []
    patch = 0
    solve(int(N), patch, [], result)
