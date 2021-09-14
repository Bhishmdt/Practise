"""
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
"""


def equilibrium(A):
    total = sum(A)
    cummsum = 0
    for i in range(len(A)):
        if cummsum == ((total - A[i]) / 2):
            return i
        cummsum += A[i]

    return -1

if __name__ == '__main__':
    A = [-7, 1, 5, 2, -4, 3, 0]
    print(equilibrium(A))
    # 3