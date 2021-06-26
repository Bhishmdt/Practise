"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""


def maxSubArray(nums):
    dp = [-float('inf')] * len(nums)
    for i in range(len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
    return max(dp)

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))
    # Returns 6