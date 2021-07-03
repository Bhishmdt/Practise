"""
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

    a 1-day pass is sold for costs[0] dollars,
    a 7-day pass is sold for costs[1] dollars, and
    a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.

    For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
"""


def mincostTickets(days, costs):
    last_day = days[-1]
    days_set = set(days)
    dp = [0 for _ in range(last_day + 1)]

    for i in range(last_day + 1):
        if i not in days_set:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(dp[max(0, i - 1)] + costs[0],
                        dp[max(0, i - 7)] + costs[1],
                        dp[max(0, i - 30)] + costs[2])
    return dp[-1]

if __name__ == '__main__':
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print(mincostTickets(days, costs))
    # Returns 11

    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    print(mincostTickets(days, costs))
    # Returns 17