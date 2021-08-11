"""
Find the shortest path in a maze.
"""

def findShortestPath(matrix, x, y):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    queue = []
    queue.append((0, 0, 0))

    while queue:
        i, j, dist = queue.pop(0)

        if i == x and j == y:
            return dist

        for d in directions:
            r = i + d[0]
            c = j + d[1]
            if r > -1 and c > -1 and r < len(matrix) and c < len(matrix[0]) and matrix[r][c] == 1:
                matrix[r][c] = '#'
                queue.append((r, c, dist + 1))
    return 0

if __name__ == '__main__':
    mat = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]

    print(findShortestPath(mat, 7, 5))
    # Returns 12