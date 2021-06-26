"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.
"""


def largestNumber(nums):
    mergeSort(nums)
    return "".join(map(str, nums))

def compare(a, b):
    return str(a) + str(b) > str(b) + str(a)


def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2

        L = A[:mid]
        R = A[mid:]

        mergeSort(L)
        mergeSort(R)

        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if compare(L[i], R[j]):
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
    nums = [3, 30, 34, 9, 5]
    print(largestNumber(nums))
    # Returns "9534330"

    nums = [111311, 1113]
    print(largestNumber(nums))
    # Returns "1113111311"

