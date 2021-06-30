"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose
elements sum up to a multiple of k, or false otherwise.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""


def checkSubarraySum(nums, k):
    d = {0: -1}
    total = 0
    for i in range(len(nums)):
        if k != 0:
            total = (total + nums[i]) % k
        else:
            total += nums[i]
        if total not in d:
            d[total] = i
        else:
            if i - d[total] >= 2:
                return True
    return False

if __name__ == '__main__':
    nums = [23, 2, 6, 4, 7]
    k = 6
    print(checkSubarraySum(nums, k))
    # Returns True

    nums = [23, 2, 6, 4, 7]
    k = 13
    print(checkSubarraySum(nums, k))
    # Returns False
