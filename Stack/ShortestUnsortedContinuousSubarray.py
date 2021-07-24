"""
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.
"""


def findUnsortedSubarray(nums):
    start = [(-float('inf'), -1)]
    end = [(float('inf'), len(nums))]
    for i in range(len(nums)):
        if start and start[-1][0] > nums[i]:
            break
        start.append((nums[i], i))

    for i in range(start[-1][1], len(nums)):
        while start and start[-1][0] > nums[i]:
            start.pop()

    for i in range(len(nums) - 1, -1, -1):
        if end and end[-1][0] < nums[i]:
            break
        end.append((nums[i], i))

    for i in range(end[-1][1], -1, -1):
        while end and end[-1][0] < nums[i]:
            end.pop()

    if end[-1][1] > start[-1][1]:
        return end[-1][1] - start[-1][1] - 1
    return 0

if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(findUnsortedSubarray(nums))
    # Returns 5

    nums = [1, 2, 3, 4]
    print(findUnsortedSubarray(nums))
    # Returns 0