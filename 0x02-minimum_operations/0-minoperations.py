#!/usr/bin/python3
"""
module for minimum operations
"""


def minOperations(n):
    """
    minimum operations function
    """
    if n <= 1:
        return 0  # No operations needed for 1 H or less
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        # Set dp[i] to i, which is the maximum number of operations needed
        dp[i] = i
        for j in range(i - 1, 0, -1):
            if i % j == 0:  # If j is a divisor of i
                dp[i] = min(dp[i], dp[j] + (i // j))
                break  # No need to check smaller divisors

    return dp[n]
