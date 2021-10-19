"""
Given two arrays of integers A[] and B[] of size N and M,
the task is to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.
"""

def swap(A, B):
    if abs((sum(A) - sum(B))) % 2 == 0:
        diff = (sum(A) - sum(B)) / 2
    else:
        return False

    S = set()

    for e in A:
        S.add(e)

    for e in B:
        if e + diff in S:
            return True
    return False

if __name__ == '__main__':
    A = [4, 1, 2, 1, 1, 2]
    B = [3, 6, 3, 3]
    print(swap(A, B))
    # True

