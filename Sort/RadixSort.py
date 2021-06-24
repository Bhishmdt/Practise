"""
Radix Sort
"""


def countingSort(A, exp):
    n = len(A)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = (A[i] / exp)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (A[i] / exp)
        output[count[int(index % 10)] - 1] = A[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(A)):
        A[i] = output[i]


def radixSort(A):
    max_num = max(A)

    exp = 1
    while max_num / exp > 0:
        countingSort(A, exp)
        exp *= 10

if __name__ == '__main__':
    A = [100, 20, 30, 3, 54, 78, 89, 453]
    radixSort(A)
    print(A)
    # Returns [3, 20, 30, 54, 78, 89, 100, 453]