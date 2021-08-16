"""
You are given two positive integer arrays nums1 and nums2, both of length n.

The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.

|x| is defined as:

    x if x >= 0, or
    -x if x < 0.

"""

import bisect


def minAbsoluteSumDiff(nums1, nums2):
    mod = 10 ** 9 + 7
    absdiffsum, absdiff = 0, []
    mi = float('inf')
    n = len(nums1)
    for i in range(n):
        diff = abs(nums1[i] - nums2[i])
        absdiffsum += diff
        absdiff.append(diff)
    nums1.sort()
    for num, diff in zip(nums2, absdiff):
        idx = bisect.bisect_left(nums1, num)
        if idx > 0:
            mi = min(mi, absdiffsum - diff + abs(num - nums1[idx - 1]))
        if idx < n:
            mi = min(mi, absdiffsum - diff + abs(num - nums1[idx]))
    return mi % mod

if __name__ == '__main__':
    nums1 = [1, 10, 4, 4, 2, 7]
    nums2 = [9, 3, 5, 1, 7, 4]
    print(minAbsoluteSumDiff(nums1, nums2))
    # 20