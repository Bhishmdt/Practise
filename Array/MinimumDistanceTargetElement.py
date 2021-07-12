"""
Given an integer array nums (0-indexed) and two integers target and start,
find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.
Return abs(i - start).
It is guaranteed that target exists in nums.
"""


def getMinDistance(nums, target, start):
    check = []
    for i in range(len(nums)):
        if nums[i] == target:
            check.append(i)
    least = len(nums) + 1
    for e in check:
        if abs(start - e) < least:
            least = abs(start - e)
    return least

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    target = 5
    start = 3
    print(getMinDistance(nums, target, start))
    # Returns 1

    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    target = 1
    start = 0
    print(getMinDistance(nums, target, start))
    # Returns 0