#!/usr/bin/python3
"""
module for minimum operations
"""


def minOperations(n):
    if n == 1:
        return 0  # No operations needed for 1 H
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:  # If j is a divisor of i
                dp[i] = min(dp[i], dp[j] + 1 + i // j - 1)

    return dp[n] if dp[n] != float('inf') else 0
