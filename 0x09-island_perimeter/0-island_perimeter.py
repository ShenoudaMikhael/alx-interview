#!/usr/bin/python3
"""Island perimeter Module"""


def island_perimeter(grid):
    """Return the perimiter of an island."""
    w = len(grid[0])
    h = len(grid)
    edge = 0
    s = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                s += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edge += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edge += 1
    return s * 4 - edge * 2
