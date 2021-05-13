"""
Find subsets of a given array
"""
from itertools import combinations

def findSubsets(A):
    """
    Recursive solution
    """
    result = []
    helper(A, [], result)
    return result

def helper(A, path, result):
    result.append(path)
    for i in range(len(A)):
        helper(A[i + 1:], path + [A[i]], result)

def findSubsets2(A):
    """
    Iterative solution
    """
    result = [[]]
    for e in A:
        for i in range(len(result)):
            result.append(result[i] + [e])
    return result

def findSubsets3(A):
    """
    Using itertools.combinations
    """
    result = []
    for i in range(len(A)+1):
        for s in combinations(A, i):
            result.append(list(s))

    return result

def findSubsets4(A):
    """
    Using bitwise operators
    """
    result = []
    for mask in range(2 ** len(A)):
        temp = []
        for i in range(len(A)):
            if mask >> i & 1:
                temp.append(A[i])
        result.append(temp)
    return result

if __name__ == '__main__':
    A = [2, 1, 4, 5]
    print(findSubsets(A))
    # [[], [2], [2, 1], [2, 1, 4], [2, 1, 4, 5], [2, 1, 5], [2, 4], [2, 4, 5], [2, 5], [1], [1, 4], [1, 4, 5], [1, 5], [4], [4, 5], [5]]

    A = [2, 1, 4, 5]
    print(findSubsets2(A))
    #  [[], [2], [1], [2, 1], [4], [2, 4], [1, 4], [2, 1, 4], [5], [2, 5], [1, 5], [2, 1, 5], [4, 5], [2, 4, 5], [1, 4, 5], [2, 1, 4, 5]]

    A = [2, 1, 4, 5]
    print(findSubsets3(A))
    # [[], [2], [1], [4], [5], [2, 1], [2, 4], [2, 5], [1, 4], [1, 5], [4, 5], [2, 1, 4], [2, 1, 5], [2, 4, 5], [1, 4, 5], [2, 1, 4, 5]]

    A = [2, 1, 4, 5]
    print(findSubsets4(A))
    # [[], [2], [1], [2, 1], [4], [2, 4], [1, 4], [2, 1, 4], [5], [2, 5], [1, 5], [2, 1, 5], [4, 5], [2, 4, 5], [1, 4, 5], [2, 1, 4, 5]]