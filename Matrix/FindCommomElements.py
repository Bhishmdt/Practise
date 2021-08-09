"""
Find all common elements present in each row of a matrix.
"""
from collections import defaultdict

def findCommon(matrix):
    d = defaultdict(int)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if d[matrix[i][j]] == i:
                d[matrix[i][j]] += 1

    return [i for i in d.keys() if d[i] == len(matrix)]


if __name__ == '__main__':
    matrix = [
        [7, 1, 3, 5, 3, 6],
        [2, 3, 6, 1, 1, 6],
        [6, 1, 7, 2, 1, 4],
        [6, 6, 7, 1, 3, 3],
        [5, 5, 6, 1, 5, 4],
        [3, 5, 6, 2, 7, 1],
        [4, 1, 4, 3, 6, 4],
        [4, 6, 1, 7, 4, 3]
    ]

    print(findCommon(matrix))
    # Returns [1, 6]