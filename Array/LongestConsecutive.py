"""
Given an array of positive integers.
Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
"""

def findLongest(A):
    S = set([e for e in A])
    result = 0

    for e in A:
        if e - 1 not in S:
            i = e
            while i in S:
                i += 1

            result = max(result, i - e)
    return result

if __name__ == '__main__':
    A = [1, 9, 3, 10, 4, 20, 2]
    print(findLongest(A))
    # 4