"""
Given an array of integers, find the length of the longest sub-array with a sum that equals 0.
"""

def findMaxSubSum(A):
    d = {}
    d[0] = -1
    result, curr = 0, 0
    for i in range(len(A)):
        curr += A[i]
        if A[i] == 0:
            result = max(1, result)
        if curr in d:
            result = max(result, i - d[curr])
        else:
            d[curr] = i
    return result

if __name__ == '__main__':
    A = [-1, 0, 1, 2]
    print(findMaxSubSum(A))
    # 3

    A = [2, 0, 1, 2]
    print(findMaxSubSum(A))
    # 1

    A = [15, -2, 2, -2, 1, 7, 10, 23]
    print(findMaxSubSum(A))
    # 2

    A = [2, 1, 2]
    print(findMaxSubSum(A))
    # 0