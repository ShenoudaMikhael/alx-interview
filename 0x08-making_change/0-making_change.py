#!/usr/bin/python3
"""makeChange Module"""


def makeChange(coins, total):
    """Make Change Function"""
    if total <= 0:
        return 0

    monc = [float("inf")] * (total + 1)
    monc[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            monc[i] = min(monc[i], monc[i - coin] + 1)

    return monc[total] if monc[total] != float("inf") else -1
