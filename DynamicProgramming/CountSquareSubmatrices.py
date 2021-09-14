"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""


def countSquares(matrix):
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1

    return sum(list(map(sum, matrix)))

if __name__ == '__main__':
    matrix =    [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    print(countSquares(matrix))
    # 15