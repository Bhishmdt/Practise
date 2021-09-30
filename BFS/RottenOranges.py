"""
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the minimum time required to rot all oranges.
A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time.
"""
from collections import deque

def rottingOranges(grid):
    count_fresh = 0
    rotten = deque()
    time_req = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                count_fresh += 1
            elif grid[r][c] == 2:
                rotten.append((r,c))

    while rotten and count_fresh > 0:
        time_req += 1

        for i in range(len(rotten)):
            x, y = rotten.popleft()
            for d in directions:
                r, c = x + d[0], y + d[1]
                if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == 1:
                    count_fresh -= 1
                    rotten.append((r, c))
                    grid[r][c] = 2

    if count_fresh == 0:
        return time_req
    else:
        return -1

if __name__ == '__main__':
    grid = [
        [0, 1, 2], 
        [0, 1, 2], 
        [2, 1, 1]
    ]
    print(rottingOranges(grid))
    # 1

    grid = [[2, 2, 0, 1]]
    print(rottingOranges(grid))
    # -1
