"""
QuickSort
"""
def partition(left, right, nums):
    pivot = right
    while left < right:
        while nums[right] >= nums[pivot] and right >= 0:
            right -= 1
        while nums[left] < nums[pivot] and left < len(nums):
            left += 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

    nums[left], nums[pivot] = nums[pivot], nums[left]
    return left

def quickSort(left, right, nums):
    if (left < right):
        p = partition(left, right, nums)
        quickSort(left, p - 1, nums)
        quickSort(p + 1, right, nums)

if __name__ == '__main__':
    A = [1, 2, 1, 8, 5, 9, 5, 2]
    quickSort(0, len(A) - 1, A)
    print(A)
    # Returns [1, 1, 2, 2, 5, 5, 8, 9]
