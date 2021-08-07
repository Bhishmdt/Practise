"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
"""


def findPaths(m, n, maxMove, startRow, startColumn):
    stack = [(startRow, startColumn, maxMove)]
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    result = 0
    while stack:
        r, c, m = stack.pop()
        print(r, c, m)
        if m < 0:
            continue
        if r < 0 or c < 0 or r > m - 1 or c > n - 1:
            result += 1
            continue
        for i, j in directions:
            stack.append((r + i, c + j, m - 1))

    return result