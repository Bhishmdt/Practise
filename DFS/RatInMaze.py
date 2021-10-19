"""
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1).
Find all possible paths that the rat can take to reach from source to destination.
The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right).
Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it
while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time.
"""

def dfs(matrix, path, result, x, y):
    if x == len(matrix) - 1 and y == len(matrix[0]) - 1:
        result.append(path)
        return

    matrix[x][y] = 0
    directions = {'D': (1, 0), 'R': (0, 1), 'U': (-1, 0), 'L': (0, -1)}

    for d in directions.keys():
        xx = x + directions[d][0]
        yy = y + directions[d][1]
        if 0 <= xx < len(matrix) and 0 <= yy < len(matrix[0]) and matrix[xx][yy] == 1:
            dfs(matrix, path + d, result, xx, yy)

    matrix[x][y] = 1

def findPaths(matrix):
    result = []
    if matrix[0][0] == 0 or matrix[-1][-1] == 0:
        return

    dfs(matrix, "", result, 0, 0)
    return result

if __name__ == '__main__':
    matrix = [[1, 0, 0, 0],
              [1, 1, 0, 1],
              [1, 1, 0, 0],
              [0, 1, 1, 1]]
    
    print(findPaths(matrix))