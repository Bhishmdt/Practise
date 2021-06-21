"""
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

    For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].

Return the minimum number of operations needed to make nums strictly increasing.
"""


def minOperations(nums):
    result = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            d = nums[i - 1] - nums[i] + 1
            result += d
            nums[i] = nums[i - 1] + 1

    return result


if __name__ == '__main__':
    print(minOperations([1, 1, 1]))
    # Returns 3

    print(minOperations([1, 5, 2, 4, 1]))
    # Returns 14