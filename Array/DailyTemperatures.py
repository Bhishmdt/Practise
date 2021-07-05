"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

def dailyTemperatures(temperatures):
    stack = []
    dp = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and stack[-1][1] < temperatures[i]:
            idx, _ = stack.pop()
            dp[idx] = i - idx
        stack.append((i, temperatures[i]))

    return dp

if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temperatures))
    # Returns [1, 1, 4, 2, 1, 1, 0, 0]

    temperatures = [30, 40, 50, 60]
    print(dailyTemperatures(temperatures))
    # Returns [1, 1, 1, 0]
    