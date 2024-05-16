#!/usr/bin/python3
"""
prime number game
implementation
"""


def sieve(n):
    """
    returns list of prime numbers up to
    n using sieve of Erastothenes
    """
    is_prime = [True] * (n + 1)
    p = 2
    while(p * p <= n):

        if (is_prime[p]):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def prime_count_up_to(n, primes):
    """
    counts up to n using prcomputed primes
    """
    count = 0
    for prime in primes:
        if prime > n:
            break
        count += 1
    return count


def isWinner(x, nums):
    """
    determines if Maria(1) OR ben (0)
    wins for given n
    """
    max_n = max(nums)
    primes = sieve(max_n)
    dp = [-1] * (max_n + 1)

    def game_winner(n):
        """
        Determine if Maria(1) or Ben(0)
        wins for a given n
        """
        if n < 2:
            return 0

        if dp[n] != -1:
            return dp[n]

        primes_count = prime_count_up_to(n, primes)
        if primes_count % 2 == 1:
            dp[n] = 1
        else:
            dp[n] = 0

        return dp[n]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = game_winner(n)
        if winner == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
