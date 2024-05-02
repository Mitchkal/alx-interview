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

    table = [float('inf')] * (total + 1)
    table[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):

            if table[i - coin] + 1 < table[i]:

                table[i] = table[i - coin] + 1

    return table[total] if table[total] != float('inf') else -1
