"""
Find the index of a row containing the maximum number of 1’s in a binary matrix (row-wise sorted).
"""


def findMaxOnesRow(matrix):

    i = 0
    n = len(matrix[0])
    m = len(matrix)
    j = n - 1
    max = 0

    while i < m and j > -1:
        if matrix[i][j] == 1:
            j -= 1
            max = i

        else:
            i += 1

    return max

if __name__ == '__main__':
    matrix = [
        [0, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1]
    ]
    print(findMaxOnesRow(matrix))
    # Returns 3

