"""
Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.
"""
from collections import deque

def findMaxOfSubarraySizeK(A, k):
    result = []
    q = deque()
    for i in range(len(A)):
        if q and i - q[0] == k:
            q.popleft()

        while q and A[q[-1]] < A[i]:
            q.pop()

        q.append(i)

        if i + 1 >= k:
            result.append(A[q[0]])

    return result

if __name__ == '__main__':
    A = [2, 5, 6, 4, 3, 2, 1, 6]
    print(findMaxOfSubarraySizeK(A, 3))
    # [6, 6, 6, 4, 3, 6]
