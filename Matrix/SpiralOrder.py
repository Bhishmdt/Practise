"""
Print matrix in spiral order.
"""

def printSpiral(matrix):
    ring = 0
    result = []
    total = 0
    while True:
        for j in range(ring, len(matrix[0]) - ring):
            result.append(matrix[ring][j])
            total += 1
            if total == len(matrix) * len(matrix[0]):
                return result
        for i in range(ring + 1, len(matrix) - ring):
            result.append(matrix[i][len(matrix[0]) - 1 - ring])
            total += 1
            if total == len(matrix) * len(matrix[0]):
                return result
        for j in range(len(matrix[0]) - ring - 1 - 1, ring - 1, -1):
            result.append(matrix[len(matrix) - 1 - ring][j])
            total += 1
            if total == len(matrix) * len(matrix[0]):
                return result
        for i in range(len(matrix) - 1 - ring - 1, ring, -1):
            result.append(matrix[i][ring])
            total += 1
            if total == len(matrix) * len(matrix[0]):
                return result
        ring += 1

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    
    print(printSpiral(matrix))
    # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]