"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
"""

def nextGreaterElements(nums):
    dp = [-1] * len(nums)
    stack = []
    maxnum = max(nums)
    maxindex = len(nums)
    for i in range(len(nums)):
        if nums[i] == maxnum:
            maxindex = i

    for i in range(maxindex - len(nums), maxindex + 1):
        while stack and nums[i] > stack[-1][0]:
            num, j = stack.pop()
            dp[j] = nums[i]
        stack.append((nums[i], i))
    return dp

if __name__ == '__main__':
    nums = [1, 2, 1]
    print(nextGreaterElements(nums))
    # Returns [2, -1, 2]

    nums = [1, 2, 3, 4, 3]
    print(nextGreaterElements(nums))
    # Returns [2, 3, 4, -1, 4]