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

    # using prime factorization:
    min_ops = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            min_ops += divisor
            n //= divisor
        divisor += 1

    return min_ops
