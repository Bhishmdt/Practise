"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
from functools import lru_cache

def coinChange(coins, amount):
    @lru_cache(None)
    def helper(amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        return min(helper(amount - coin) + 1 for coin in coins)

    if helper(amount) == float("inf"):
        return -1
    return helper(amount)

if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))
    # Returns 3

    coins = [3, 6, 7, 2]
    amount = 354
    print(coinChange(coins, amount))
    # Returns 51