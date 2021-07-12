"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).
The rain starts to fall. At time t, the depth of the water everywhere is t.
You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t.
You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.
Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
"""
import heapq

def swimInWater(grid):
    m, n = len(grid), len(grid[0])
    time = [[float('inf')] * m for _ in range(n)]
    time[0][0] = grid[0][0]
    heap = [(grid[0][0], 0, 0)]
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while heap:
        timeij, i, j = heapq.heappop(heap)
        if i == m - 1 and j == n - 1:
            return timeij
        for k in range(4):
            x, y = i + directions[k][0], j + directions[k][1]
            if 0 <= x < m and 0 <= y < n:
                timedash = max(timeij, grid[x][y])
                if time[x][y] > timedash:
                    time[x][y] = timedash
                    heapq.heappush(heap, (time[x][y], x, y))

if __name__ == '__main__':
    grid = [[0, 2], [1, 3]]
    print(swimInWater(grid))
    # Returns 3

    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    print(swimInWater(grid))
    # Returns 16