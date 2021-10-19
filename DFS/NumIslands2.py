"""
Given a grid consisting of '0's(Water) and '1's(Land). Find the number of islands.
Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.
"""


def numIslands(grid):
    def dfs(i, j, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != '1':
            return
        grid[i][j] = 'V'
        dfs(i + 1, j, grid)
        dfs(i + 1, j + 1, grid)
        dfs(i + 1, j - 1, grid)
        dfs(i - 1, j, grid)
        dfs(i - 1, j + 1, grid)
        dfs(i - 1, j - 1, grid)
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
            ["0", "0", "0", "1", "1"]]

    print(numIslands(grid))
    # Returns 2

    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]

    print(numIslands(grid))
    # Returns 1