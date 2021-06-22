"""
MergeSort
"""

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2

        L = A[:mid]
        R = A[mid:]
        
        mergeSort(L)
        mergeSort(R)

        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

if __name__ == '__main__':
    A = [10, 4, 7, 2, 9, 1]
    mergeSort(A)
    print(A)
    # Returns [1, 2, 4, 7, 9, 10]

