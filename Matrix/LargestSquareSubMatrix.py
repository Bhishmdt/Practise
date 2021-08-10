"""
Find the largest square submatrix which is surrounded by all 1’s.
"""

def findLargestSquareMatrix(matrix):
    X = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    Y = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                Y[i][j] = (0 if i == 0 else Y[i - 1][j]) + 1
                X[i][j] = (0 if j == 0 else X[i][j - 1]) + 1
    max_len = 0
    for i in range(len(matrix) - 1, 0, -1):
        for j in range(len(matrix[0]) - 1, 0, -1):
            length = min(X[i][j], Y[i][j])
            while length:
                isSquare = X[i - length + 1][j] >= length and Y[i][j - length + 1] >= length

                if isSquare and max_len < length:
                    max_len = length

                length -= 1

    return max_len

if __name__ == '__main__':
    mat = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 1],
        [0, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]
    ]

    print(findLargestSquareMatrix(mat))
    # Returns 4
