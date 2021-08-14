"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
"""


def uniquePathsWithObstacles(obstacleGrid):
    dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
    dp[0][0] = 1 - obstacleGrid[0][0]
    for i in range(1, len(obstacleGrid)):
        dp[i][0] = dp[i - 1][0] * (1 - obstacleGrid[i][0])
    for j in range(1, len(obstacleGrid[0])):
        dp[0][j] = dp[0][j - 1] * (1 - obstacleGrid[0][j])
    for i in range(1, len(obstacleGrid)):
        for j in range(1, len(obstacleGrid[0])):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) * (1 - obstacleGrid[i][j])
    return dp[-1][-1]


if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(uniquePathsWithObstacles(obstacleGrid))
    # Returns 2