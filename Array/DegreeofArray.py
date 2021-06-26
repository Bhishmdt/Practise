"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
"""


def findShortestSubArray(nums):
    first, count, res, degree = {}, {}, 0, 0
    for i, a in enumerate(nums):
        first.setdefault(a, i)
        count[a] = count.get(a, 0) + 1
        if count[a] > degree:
            degree = count[a]
            res = i - first[a] + 1
        elif count[a] == degree:
            res = min(res, i - first[a] + 1)
    return res

if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1]
    print(findShortestSubArray(nums))
    # Returns 2

    nums = [1, 2, 2, 3, 1, 4, 2]
    print(findShortestSubArray(nums))
    # Returns 6