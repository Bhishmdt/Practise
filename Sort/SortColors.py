"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
"""


def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    r, b = 0, len(nums) - 1
    w = 0
    while w <= b:
        if nums[w] < 1:
            nums[w], nums[r] = nums[r], nums[w]
            r += 1
            w += 1
        elif nums[w] > 1:
            nums[w], nums[b] = nums[b], nums[w]
            b -= 1
        else:
            w += 1
    print(nums)

if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    sortColors(nums)
    # Returns [0, 0, 1, 1, 2, 2]