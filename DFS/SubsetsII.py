"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
"""


def subsetsWithDup(nums):
    result = []
    nums.sort()

    def dfs(nums, path, result):
        result.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            dfs(nums[i + 1:], path + [nums[i]], result)

    dfs(nums, [], result)

    return result

if __name__ == '__main__':
    nums = [1, 2, 2]
    print(subsetsWithDup(nums))
    # Returns [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    nums = [4, 1, 4, 4]
    print(subsetsWithDup(nums))
    # Returns [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [4], [4, 4], [4, 4, 4]]