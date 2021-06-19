"""
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
"""

def findTargetSumWays(nums, target):
    index = 0
    currsum = 0
    memo = {}
    return dp(nums, target, index, currsum, memo)

def dp(nums, target, index, currsum, memo):
    if (index, currsum) in memo:
        return memo[(index, currsum)]

    # If index is out of bounds and currsum is equal to target, return 1
    if index > len(nums) - 1 and currsum == target:
        return 1
    if index > len(nums) - 1:
        return 0

    # memoise current index, currsum for both + and -
    memo[(index, currsum)] = dp(nums, target, index + 1, currsum + nums[index], memo) + dp(nums, target, index + 1, currsum - nums[index], memo)
    return memo[(index, currsum)]

if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(findTargetSumWays(nums, target))
    # Returns 5

    nums = [1, 2, 3, 1, 2]
    target = 5
    print(findTargetSumWays(nums, target))
    # Return 3