"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
"""


def minPathSum(grid):
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if i > 0 and j > 0:
                grid[i][j] = min(grid[i][j] + grid[i][j - 1], grid[i][j] + grid[i - 1][j])
            elif j > 0:
                grid[i][j] = grid[i][j] + grid[i][j - 1]
            elif i > 0:
                grid[i][j] = grid[i][j] + grid[i - 1][j]

    return grid[-1][-1]

if __name__ == '__main__':
    grid = [[1,2,3],[4,5,6]]
    print(minPathSum(grid))
    # Prints 12

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(minPathSum(grid))
    # Prints 7