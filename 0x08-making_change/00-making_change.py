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

    if total <= 0:
        return 0

    # coin length list
    m = len(coins)

    table = [-1] * (total + 1)
    return utility(coins, m, total, table)


def utility(coins, m, total, table):
    """
    solves the minimum coin problem recursively
    """
    if total <= 0:
        return 0

    if table[total] != -1:
        return table[total]

    no_coins = sys.maxsize

    for j in range(m):

        if coins[j] <= total:

            combo = utility(coins, m, total - coins[j], table)

            if combo != sys.maxsize and combo + 1 < no_coins:
                no_coins = combo + 1

    table[total] = no_coins
    return no_coins
