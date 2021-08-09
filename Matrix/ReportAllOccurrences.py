"""
Report all occurrences of an element in a row-wise and column-wise sorted matrix in linear time.
"""

def reportOccurrences(matrix, target):
    i = 0
    n = len(matrix[0])
    j = n - 1

    while i < len(matrix) and j > -1:
        if matrix[i][j] == target:
            print(f"Element {target} is found at position ({i} , {j})")
            i += 1
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1

if __name__ == '__main__':
    matrix = [
        [-4, -3, -1, 3, 5],
        [-3, -2, 2, 4, 6],
        [-1, 1, 3, 5, 8],
        [3, 4, 7, 8, 9]
    ]
    target = 3
    
    reportOccurrences(matrix, target)

    """
    Element 3 is found at position (0 , 3)
    Element 3 is found at position (2 , 2)
    Element 3 is found at position (3 , 0)
    """