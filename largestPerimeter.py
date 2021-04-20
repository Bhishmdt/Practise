'''
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths.
If it is impossible to form any triangle of a non-zero area, return 0.
'''
def largestPerimeter(A):
    #sort A in reverse order
    A.sort()
    A = A[::-1]
    i = 0
    while i < len(A) - 2:
        if A[i] < A[i + 1] + A[i + 2]: # If A[i] > A[i + 1] + A[i + 2], then A[i] > any other pair
            return A[i] + A[i + 1] + A[i + 2]
        i += 1
    return 0


if __name__ == '__main__':

    A = [1, 2, 1]
    print(largestPerimeter(A))
    # result 0

    A = [3, 2, 3, 4]
    print(largestPerimeter(A))
    # result 10
