"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""


def findDuplicate(nums):
    slow, fast = nums[0], nums[0]
    while True:
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow

if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    print(findDuplicate(nums))
    # 2
