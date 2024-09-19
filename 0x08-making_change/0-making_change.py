#!/usr/bin/python3
"""makeChange Module"""


def makeChange(coins, total):
    """Make Change Function"""
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    cc = 0
    for i in coins:
        if total % i == 0:
            cc += int(total / i)
            return cc
        if total - i >= 0:
            if int(total / i) > 1:
                cc += int(total / i)
                total = total % i
            else:
                cc += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return cc
