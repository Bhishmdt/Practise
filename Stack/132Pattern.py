"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""


def find132pattern(nums):
    minarray = [nums[0]]
    for i in range(1, len(nums)):
        minarray.append(min(nums[i], minarray[-1]))
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > minarray[i]:
            while stack and stack[-1] <= minarray[i]:
                stack.pop()
            if stack and stack[-1] < nums[i]:
                return True
            stack.append(nums[i])
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(find132pattern(nums))
    # Returns False

    nums = [3, 1, 4, 2]
    print(find132pattern(nums))
    # Returns True

    nums = [-1, 3, 2, 0]
    print(find132pattern(nums))
    # Returns True
