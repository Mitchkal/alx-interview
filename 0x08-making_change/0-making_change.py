#!/usr/bin/python3
"""
finding the minimum nuber of coins needed to
meet a given amount
"""
import sys


def makeChange(coins, total):
    """
    function to find fewest number of cains in
    a given total
    """
    if total < 0:
        return 0

    # coin length list
    m = len(coins)

    table = [sys.maxsize] * (total + 1)
    table[0] = 0

    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                combo = table[i - coins[j]]
                if combo != sys.maxsize and combo + 1 < table[i]:
                    table[i] = combo + 1

    return table[total] if table[total] != sys.maxsize else -1
