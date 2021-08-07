"""
Given a matrix M x N binary matrix, replace all 0 by 1, which are not surrounded by 1.
"""

def replaceZeroes(matrix):
    def dfs(i, j):
        directions = (1, 0), (1, 1), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)
        if i < 0 or j < 0 or i > len(matrix) - 1 or j > len(matrix[0]) - 1:
            return
        if matrix[i][j] == 0:
            matrix[i][j] = 1
            for d in directions:
                dfs(i + d[0], j + d[1])
        if matrix[i][j] == 1:
            return
        
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            dfs(i, 0)
        if matrix[i][len(matrix[0]) - 1] == 0:
            dfs(i, len(matrix[0]) - 1)
    
    for j in range(len(matrix)):
        if matrix[0][j] == 0:
            dfs(0, j)
        if matrix[len(matrix) - 1][j] == 0:
            dfs(len(matrix) - 1, j)
    
    return matrix

if __name__ == '__main__':
    matrix = [
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        ]
    
    print(replaceZeroes(matrix))
    """
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1], 
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1], 
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 1], 
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    """