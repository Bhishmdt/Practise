"""
Find the number of ways to travel from start to end of a grid.
Condition: Can only move right or down from current cell.
"""

def gridTraveler(m, n, memo = {}):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[(m, n)] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[(m, n)]

if __name__ == '__main__':

    print(gridTraveler(3, 2))
    # Returns 3
    print(gridTraveler(1, 1))
    # Returns 1
    print(gridTraveler(18, 18))
    # Returns 2333606220