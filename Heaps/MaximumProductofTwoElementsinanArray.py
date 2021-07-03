"""
Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""


def maxProduct(nums):
    import heapq
    result = 1
    nums = [1 - e for e in nums]
    heapq.heapify(nums)

    for i in range(2):
        result *= heapq.heappop(nums)

    return result

if __name__ == '__main__':
    nums = [3, 4, 5, 2]
    print(maxProduct(nums))
    # Returns 12