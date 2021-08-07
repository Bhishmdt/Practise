"""
Change all elements of row and column in a matrix to 0 if cell has a value 0.
"""

def changeElements(matrix):
    r = set()
    c = set()
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                r.add(i)
                c.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in r or j in c:
                matrix[i][j] = 0

    return matrix

if __name__ == '__main__':
    matrix = [[1, 2, 3, 0],
              [5, 0, 7, 8],
              [9, 10, 11, 12],
              [0, 1, 2, 3]]
    print(changeElements(matrix))
    """
    [[0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 11, 0], 
    [0, 0, 0, 0]]
    """