#!/usr/bin/python3
"""
A script that find that winner to the prime numbers gmae
"""


def isWinner(x, nums):
    """
    Returns the winner
    """
    def is_prime(n):
        """
        Checks if n is a prime number
        """
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def can_win(n):
        if n <= 1:
            return False
        if n % 2 == 0:
            return True
        return not is_prime(n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
