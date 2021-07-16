"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
 More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
 It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
"""


def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    prev = 2
    next_num = 2

    while next_num < len(nums):
        if nums[prev - 2] != nums[next_num]:
            nums[prev] = nums[next_num]
            prev += 1
        next_num += 1
    return prev

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    print(removeDuplicates(nums), nums)
    # Returns 5 [1, 1, 2, 2, 3, 3]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(removeDuplicates(nums), nums)
    # Returns 7 [0, 0, 1, 1, 2, 3, 3, 3, 3]