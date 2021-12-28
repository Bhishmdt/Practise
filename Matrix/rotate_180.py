"""
In-place rotate matrix by 180 degrees, in clockwise direction.
"""

def rotate180(matrix):
    for i in range(len(matrix) // 2):
        for j in range(len(matrix)):
            matrix[i][j], matrix[~i][~j] = matrix[~i][~j], matrix[i][j]
    print(matrix)

    if len(matrix) // 2 == 0:
        i = len(matrix) // 2
        for j in range(len(matrix)):
            matrix[i][j], matrix[~i][~j] = matrix[~i][~j], matrix[i][j]

    return matrix

if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print(rotate180(matrix))

    """
    [
    [16, 15, 14, 13], 
    [12, 11, 10, 9], 
    [8, 7, 6, 5], 
    [4, 3, 2, 1]
    ]
    """