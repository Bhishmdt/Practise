"""
Given a matrix of N * M. Find the maximum path sum in matrix. The maximum path is sum of all elements from first row to last row where you are allowed to move only down or diagonally to left or right. You can start from any element in first row.
"""

def findMaxPath(mat):
    if len(mat) == 1:
        return max[0][:]
    for i in range(1, len(mat)):
        for j in range(len(mat[0])):
            if j > 0 and j < len(mat[0]) - 1:
                mat[i][j] += max(mat[i - 1][j - 1], mat[i - 1][j], mat[i - 1][j + 1])
            if j == 0:
                mat[i][j] += max(mat[i - 1][j], mat[i - 1][j + 1])
            if j == len(mat[0]) - 1:
                mat[i][j] += max(mat[i - 1][j - 1], mat[i - 1][j])
    return max(mat[-1][:])

if __name__ == '__main__':
    mat = ([[10, 10, 2, 0, 20, 4],
            [1, 0, 0, 30, 2, 5],
            [0, 10, 4, 0, 2, 0],
            [1, 0, 2, 20, 0, 4]])

    print(findMaxPath(mat))
    # 74