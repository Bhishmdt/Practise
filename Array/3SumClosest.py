"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
"""


def threeSumClosest(nums, target):
    result = float('inf')
    nums.sort()

    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1

        while l < r:
            currsum = nums[i] + nums[l] + nums[r]

            if abs(currsum - target) < abs(result - target):
                result = currsum

            if currsum > target:
                r -= 1
            if currsum < target:
                l += 1
            if currsum == target:
                return currsum
    return result

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    print(threeSumClosest(nums, target))
    # Returns 2