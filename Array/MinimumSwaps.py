"""
Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.
"""

def min_swaps(nums):
    S = nums.copy()
    S.sort()

    d = {e: i for i, e in enumerate(nums)}
    swaps = 0

    for i in range(len(nums)):
        if nums[i] != S[i]:
            swaps += 1
            temp = nums[i]
            nums[i], nums[d[S[i]]] = nums[d[S[i]]], nums[i]
            d[temp] = d[S[i]]
            d[S[i]] = i

    return swaps

if __name__ == '__main__':
    nums = [2, 8, 5, 4]
    print(min_swaps(nums))
    # 1

    nums = [10, 19, 6, 3, 5]
    print(min_swaps(nums))
    # 2

    nums = [19, 10, 6, 3, 5]
    print(min_swaps(nums))
    # 3
