"""
Rotate matrix in-place
"""

def invertMatrix(matrix):
    n = len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i + j < len(matrix):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]

    for i in range(len(matrix) // 2):
        for j in range(len(matrix)):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - i - 1][j], matrix[i][j]

    return matrix


if __name__ == '__main__':
    matrix = [[1, 2, 3, 10],
              [4, 5, 6, 11],
              [7, 8, 9, 12],
              [13, 14, 15, 16]]
    print(invertMatrix(matrix))
    """
    [[13, 7, 4, 1],
     [14, 8, 5, 2],
     [15, 9, 6, 3], 
     [16, 12, 11, 10]]
    """
