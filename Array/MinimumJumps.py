"""
Given an array of non-negative integers, A, of length N, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Return the minimum number of jumps required to reach the last index.
If it is not possible to reach the last index, return -1.
"""


def jump(A):
    if len(A) == 1:
        return 0

    reach, prev = 0, 0
    n_jumps = 0

    for i in range(len(A)):
        reach = max(reach, i + A[i])

        if i > prev:
            return -1

        if reach >= len(A) - 1:
            return n_jumps + 1

        if i == prev:
            prev = reach
            n_jumps += 1


if __name__ == '__main__':
    A = [2, 1, 1]
    print(jump(A))
    # 1

    A = [2, 3, 1, 1, 4]
    print(jump(A))
    # 2

    A = [2, 0, 0, 3, 1]
    print(jump(A))
    # -1

