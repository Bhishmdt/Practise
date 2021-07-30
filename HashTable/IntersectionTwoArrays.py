"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
"""
import collections

def intersection(nums1, nums2):
    d = collections.defaultdict(int)
    for e in nums1:
        d[e] = 1
    result = []
    for e in nums2:
        if d[e] == 1:
            d[e] += 1
            result.append(e)
    return result

if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersection(nums1, nums2))
    # Returns [2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(intersection(nums1, nums2))
    # Returns [9, 4]