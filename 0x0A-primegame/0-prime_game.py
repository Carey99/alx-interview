#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Maria and Ben are playing a game. Given a set of n integers,
    they have to choose the prime numbers from the set. At each turn,
    a player selects a prime number and removes that number and its
    multiples from the set. The player that cannot make a move loses
    and the other player is the winner. They play t games. Maria always
    starts. Assuming both players play optimally, determine who the
    winner is for each game.
    Args:
        n (int): the number of integers in the set
    Returns:
        str: the name of the player that won the most games
    """

    def prime(n):
        """Check if a number is prime
        Args:
            n (int): the number to check
        Returns:
            bool: True if n is prime, False otherwise
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if x < 1:
        return None

    prime_nums = []
    for i in range(1, max(nums) + 1):
        if prime(i):
            prime_nums.append(i)

    wins = 0
    for n in nums:
        wins += n in prime_nums

    if wins % 2 == 0:
        return "Maria"
    return "Ben"
