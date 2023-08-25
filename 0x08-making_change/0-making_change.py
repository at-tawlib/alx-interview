#!/usr/bin/python3
"""
Making change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, we determine
    the fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
