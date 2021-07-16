"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
"""


def subsets(nums):
    result = []

    def dfs(nums, path, result):
        result.append(path)
        for i in range(len(nums)):
            dfs(nums[i + 1:], path + [nums[i]], result)

    dfs(nums, [], result)
    return result

if __name__ == '__main__':
    nums = [1,2,3]
    print(subsets(nums))
    # Returns [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]