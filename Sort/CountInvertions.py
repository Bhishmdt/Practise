"""
Invertion Count for an array indicates - how far the array is from being sorted. If the array is already sorted, then invertion count is 0.
"""

def countInvertion(arr):
    l, r, count = 0, 0, 0
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        l = countInvertion(L)
        r = countInvertion(R)

        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                count += mid - i
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return count + l + r

if __name__ == '__main__':
    arr = [10, 20, 4, 5, 6]
    print(countInvertion(arr))