"""
Heap Sort
"""

def heapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[largest] < A[l]:
        largest = l

    if r < n and A[largest] < A[r]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        print(A)

        heapify(A, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == '__main__':
    A = [1, 7, 3, 9, 4, 7]
    heapSort(A)