"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
"""


def maxProfit(prices):
    result = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            result += prices[i] - prices[i - 1]

    return result

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
    # Returns 7