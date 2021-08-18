"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""


def longestOnes(nums, k):
    start = 0
    for i in range(len(nums)):
        if not nums[i]:
            k -= 1
        if k < 0:
            if not nums[start]:
                k += 1
            start += 1
    return i - start + 1

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    print(longestOnes(nums, k))
    # 10