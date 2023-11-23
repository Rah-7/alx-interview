def makeChange(coins, total):
    if total < 0:
        return -1
    if total == 0:
        return 0

    dp =  * (total + 1)
    dp = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp = min(dp, dp + 1)

    return dp if dp != float('inf') else -1
