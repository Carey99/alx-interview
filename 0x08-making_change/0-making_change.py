#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    bal = total
    count = 0
    idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while bal > 0:
        if idx >= n:
            return -1
        if bal - sorted_coins[idx] >= 0:
            bal -= sorted_coins[idx]
            count += 1
        else:
            idx += 1
    return count
