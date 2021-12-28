"""
Given two integer arrays A1 and A2, sort A1 in such a way that the relative order among the elements will be same as those are in A2.

For the elements that are not in A2, append them in the right end of the A1 in an ascending order.

Assumptions:

    A1 and A2 are both not null.
    There are no duplicate elements in A2.

"""
def compare(a, b, d):
    if a in d.keys() and b in d.keys():
        return True if d[a] < d[b] else False
    else:
        return True if a < b else False

def mergeSort(A, B):
    d = {B[i]:i for i in range(len(B))}
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        mergeSort(L, B)
        mergeSort(R, B)

        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if compare(L[i], R[j], d):
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
    A1 = [2, 1, 2, 5, 7, 1, 9, 3]
    A2 = [2, 1, 3]
    mergeSort(A1, A2)
    print(A1)

