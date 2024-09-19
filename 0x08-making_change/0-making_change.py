#!/usr/bin/python3
""" Contains makeChange function"""


def makeChange(coins, total):
    """Make Change Function"""
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for change in coins:
        while change <= total:
            total -= change
            change += 1
        if total == 0:
            return change
    return -1
