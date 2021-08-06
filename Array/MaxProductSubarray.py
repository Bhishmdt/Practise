"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""


def maxProduct(nums):

    rev = nums[::-1]
    for i in range(1, len(nums)):
        nums[i] *= nums[i - 1] or 1
        rev[i] *= rev[i - 1] or 1

    return max(rev + nums)

if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    print(maxProduct(nums))
    # Returns 6

    nums = [-2, 0, -1]
    print(maxProduct(nums))
    # Returns 0
