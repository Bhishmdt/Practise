"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
"""

def numTrees(n):
    return factorial(2 * n) // factorial(n) // factorial(n) // (n + 1)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    print(numTrees(6)
    # 132
