"""
Print all shortest routes in a rectangular grid.
"""

def printPaths(matrix):
    allPaths = []

    def helper(matrix, path, i, j):
        if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
            allPaths.append(path + [matrix[i][j]])

        if i + 1 < len(matrix):
            helper(matrix, path + [matrix[i][j]], i + 1, j)

        if j + 1 < len(matrix[0]):
            helper(matrix, path + [matrix[i][j]], i, j + 1)

        if i + 1 < len(matrix) and j + 1 < len(matrix[0]):
            helper(matrix, path + [matrix[i][j]], i + 1, j + 1)

    helper(matrix, [], 0, 0)
    print(allPaths)

if __name__ == '__main__':
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    printPaths(mat)
    """
    [
    [1, 4, 7, 8, 9], 
    [1, 4, 5, 8, 9], 
    [1, 4, 5, 6, 9], 
    [1, 4, 5, 9], 
    [1, 4, 8, 9], 
    [1, 2, 5, 8, 9], 
    [1, 2, 5, 6, 9], 
    [1, 2, 5, 9], 
    [1, 2, 3, 6, 9], 
    [1, 2, 6, 9], 
    [1, 5, 8, 9], 
    [1, 5, 6, 9], 
    [1, 5, 9]
    ]
    """
