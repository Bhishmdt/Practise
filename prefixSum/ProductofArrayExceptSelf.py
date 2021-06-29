"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""


def productExceptSelf(nums):
    mul = 1
    d_before = {0: 1}
    d_after = {(len(nums) - 1): 1}
    for i in range(1, len(nums)):
        mul *= nums[i - 1]
        d_before[i] = mul
    mul = 1
    for i in range(len(nums) - 2, -1, -1):
        mul *= nums[i + 1]
        d_after[i] = mul
    result = []
    for i in range(len(nums)):
        result.append(d_before[i] * d_after[i])
    return result

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))
    # Returns [24,12,8,6]

    nums = [-1, 1, 0, -3, 3]
    print(productExceptSelf(nums))
    # Returns [0, 0, 9, 0, 0]
