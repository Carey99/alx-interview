#!/usr/bin/python3
'''takes high, value and lst'''


def makeChange(coins, total):
    if total == 0:
        return 0
    if total < 0:
        return -1

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total <= 0:
            break
        use_coin = total // coin
        count += use_coin
        total -= use_coin * coin

    return count if total == 0 else -1
