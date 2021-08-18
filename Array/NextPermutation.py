"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
"""


def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1
    if i == 0:
        nums.reverse()
        return
    j = i
    while j + 1 < len(nums) and nums[j + 1] > nums[i - 1]:
        j += 1
    nums[j], nums[i - 1] = nums[i - 1], nums[j]
    nums[i:] = nums[i:][::-1]
    
if __name__ == '__main__':
    nums = [1, 2, 3]
    nextPermutation(nums)
    print(nums)
    # [1, 3, 2]