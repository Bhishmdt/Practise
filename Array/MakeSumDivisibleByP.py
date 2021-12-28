"""
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p.
It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.
"""


def minSubarray(nums, p):
    dic = {0: -1}
    result = float('inf')
    target = sum(nums) % p
    currsum = 0
    for i in range(len(nums)):
        currsum = (currsum + nums[i]) % p
        dic[currsum] = i
        if (currsum - target) % p in dic:
            result = min(result, i - dic[(currsum - target) % p])
    if result >= len(nums):
        return -1
    return result

if __name__ == '__main__':
    nums = [3, 1, 4, 2]
    p = 6
    print(minSubarray(nums, p))
    # Returns 1

    nums = [6, 3, 5, 2]
    p = 9
    print(minSubarray(nums, p))
    # Returns 2