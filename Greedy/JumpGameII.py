"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.
"""


def jump(nums):
    if len(nums) == 1:
        return 0

    reach, prev = 0, 0
    n_jumps = 0

    for i in range(len(nums)):
        reach = max(reach, i + nums[i])
        print(i, reach)

        if reach >= len(nums) - 1:
            return n_jumps + 1

        if i == prev:
            prev = reach
            n_jumps += 1

    return n_jumps

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(jump(nums))
    # Returns 2

    nums = [2, 5, 3, 1, 1, 2, 1, 1, 2]
    print(jump(nums))
    # Returns 4