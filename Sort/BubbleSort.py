"""
Bubble Sort
"""

def bubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A) - i -1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


if __name__ == '__main__':
    A = [10, 67, 2, 33, 22, 56, 22]
    bubbleSort(A)
    print(A)
    # Returns [2, 10, 22, 22, 33, 56, 67]