"""
Given an array of integers and another number. Find all the unique quadruple from the given array that sums up to the given number.
"""

def fourSum(A, K):
    A.sort()
    result = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            l, r = j + 1, len(A) - 1
            balance = K - A[i] - A[j]
            while l < r:
                if A[l] + A[r] == balance:
                    result.append((A[i], A[j], A[l], A[r]))
                    l, r = l + 1, r - 1
                elif A[l] + A[r] > balance:
                    r -= 1
                else:
                    l += 1
    return set(result)

if __name__ == '__main__':
    A = [10, 2, 3, 4, 5, 5, 7, 8]
    K = 23
    print(fourSum(A, K))
