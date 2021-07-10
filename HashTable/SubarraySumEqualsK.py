"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
"""


def subarraySum(nums, k):
    result = 0
    d = {}
    d[0] = 1
    currsum = 0
    for e in nums:
        currsum += e
        result += d.get(currsum - k, 0)
        d[currsum] = d.get(currsum, 0) + 1
    return result

if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    print(subarraySum(nums, k))
    # Returns 2

    nums = [-1, -1, 1, 0]
    k = 0
    print(subarraySum(nums, k))
    # Retuns 3