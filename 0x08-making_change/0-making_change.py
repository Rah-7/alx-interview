#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins >= 0:  # Fix: Access coin value at current index
            rem -= sorted_coins  # Fix: Subtract coin value at current index
            coins_count += 1
        else:
            coin_idx += 1  # Fix: Increment coin index
    if rem > 0:
        return -1
    else:
        return coins_count
