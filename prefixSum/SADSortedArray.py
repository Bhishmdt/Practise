"""
You are given an integer array nums sorted in non-decreasing order.
Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of
absolute differences between nums[i] and all the other elements in the array.
In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).
"""


def getSumAbsoluteDifferences(nums):
    total = sum(nums)
    n = len(nums)
    result = []

    for i, num in enumerate(nums):
        result.append(total - (n - i) * num + i * num)
        total -= 2 * num

    return result

if __name__ == '__main__':
    nums = [2, 3, 5]
    print(getSumAbsoluteDifferences(nums))
    # Returns [4, 3, 5]

    nums = [1, 4, 6, 8, 10]
    print(getSumAbsoluteDifferences(nums))
    # Returns [24, 15, 13, 15, 21]