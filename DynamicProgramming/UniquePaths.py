"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
"""


def uniquePaths(m, n):
    if not m or not n:
        return 0
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

if __name__ == '__main__':
    m = 7
    n = 3
    print(uniquePaths(m, n))
    # Returns 28

    m = 3
    n = 3
    print(uniquePaths(m, n))
    # Returns 6