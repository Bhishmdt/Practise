"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
"""


def canJump(nums):
    can_reach = 0
    for i in range(len(nums)):
        can_reach = max(i + nums[i], can_reach)
        # If can_reach is greater than last index, return True
        if can_reach >= len(nums) - 1:
            return True
        # If anywhere current number is 0 and you can reach to that index or lower, return False
        if nums[i] == 0 and can_reach <= i:
            return False

if __name__ == '__main__':
    print(canJump([3, 2, 0, 5]))
    #Returns True
    print(canJump([3, 2, 1, 0, 5]))
    #Returns False