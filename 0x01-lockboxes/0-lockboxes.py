#!/usr/bin/python3
"""Lock Boxes Module"""


def canUnlockAll(boxes):
    """can Unlock All"""
    n = len(boxes)
    unlocked = set()
    unlocked.add(0)

    stack = [0]

    while stack:
        box_index = stack.pop()
        for key in boxes[box_index]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
