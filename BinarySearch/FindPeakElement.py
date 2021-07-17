"""
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.
"""


def findPeakElement(nums):
    if len(nums) == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return len(nums) - 1
    start = 1
    end = len(nums) - 2

    while start <= end:
        mid = (start + end) // 2
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid - 1] > nums[mid]:
            end = mid - 1
        elif nums[mid + 1] > nums[mid]:
            start = mid + 1
    return -1

if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(findPeakElement(nums))
    # Returns 2

    nums = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(nums))
    # Returns 5