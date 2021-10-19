"""
Given an array of N integers. Find the first element that occurs K number of times.
"""

def findFirst(A, K):
    d = {}
    for e in A:
        d[e] = d.get(e, 0) + 1
        if d[e] == K:
            return e
    return -1

if __name__ == '__main__':
    A = [1, 7, 4, 3, 4, 8, 7]
    print(findFirst(A, 2))
    # 4

    A = [1, 7, 4, 3, 4, 8, 7]
    print(findFirst(A, 3))
    # -1

