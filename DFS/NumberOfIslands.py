"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


def numIslands(grid):
    def dfs(i, j, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != '1':
            return
        grid[i][j] = 'V'
        dfs(i + 1, j, grid)
        dfs(i - 1, j, grid)
        dfs(i, j + 1, grid)
        dfs(i, j - 1, grid)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                dfs(i, j, grid)
                count += 1
    return count

if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    
    print(numIslands(grid))
    # Returns 1

    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]

    print(numIslands(grid))
    # Returns 3