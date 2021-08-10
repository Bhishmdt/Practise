"""
Find maximum value of `M[c][d] – M[a][b]` over all choices of indexes. (c>a and d>b)
"""

def findMaxDiff(matrix):
    T = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    N = len(matrix)
    T[N - 1][N - 1] = matrix[N - 1][N - 1]

    max_num = matrix[N - 1][N - 1]
    for i in range(N - 2, -1, -1):
        if max_num < matrix[i][N - 1]:
            max_num = matrix[i][N - 1]
        T[i][N - 1] = max_num

    max_num = matrix[N - 1][N - 1]
    for j in range(N - 2, -1, -1):
        if max_num < matrix[N - 1][j]:
            max_num = matrix[N - 1][j]
        T[N - 1][j] = max_num

    max_diff = -float('inf')
    for i in range(N - 2, -1, -1):
        for j in range(N - 2, -1, -1):
            if T[i + 1][j + 1] - matrix[i][j] > max_diff:
                max_diff = T[i + 1][j + 1] - matrix[i][j]

            T[i][j] = max(matrix[i][j], T[i + 1][j], T[i][j + 1])

    return max_diff

if __name__ == '__main__':
    M = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 6, 1, 3],
        [-4, -1, 1, 7, -6],
        [0, -4, 10, -5, 1]
    ]

    print(findMaxDiff(M))
    # Returns 18