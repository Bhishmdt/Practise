"""
Bucket Sort
"""

def insertionSort(A):
    for i in range(1, len(A)):
        temp = A[i]
        j = i - 1
        while j >= 0 and A[j] > temp:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = temp
    return A

def buscketSort(A):
    slot_num = 10
    arr = [[] for _ in  range(slot_num)]

    for e in A:
        index = int(slot_num * e)
        arr[index].append(e)

    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            A[k] = arr[i][j]
            k += 1
    return A

if __name__ == '__main__':
    A = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(buscketSort(A))
    # Returns [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]