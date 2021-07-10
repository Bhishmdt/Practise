"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,
where heights[row][col] represents the height of cell (row, col). You are situated in the
top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed).
You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
"""
from heapq import heappush, heappop

def minimumEffortPath(heights):
    m, n = len(heights), len(heights[0])
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while heap:
        print(heap, dist)
        d, i, j = heappop(heap)
        if d > dist[i][j]:
            continue
        if i == m - 1 and j == n - 1:
            return d
        for k in range(4):
            x, y = i + directions[k][0], j + directions[k][1]
            if 0 <= x < m and 0 <= y < n:
                newDist = max(d, abs(heights[x][y] - heights[i][j]))
                if dist[x][y] > newDist:
                    dist[x][y] = newDist
                    heappush(heap, (dist[x][y], x, y))

if __name__ == '__main__':
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(minimumEffortPath(heights))