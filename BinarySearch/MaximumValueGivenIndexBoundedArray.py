"""
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

    nums.length == n
    nums[i] is a positive integer where 0 <= i < n.
    abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
    The sum of all the elements of nums does not exceed maxSum.
    nums[index] is maximized.

Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.
"""


def maxValue(n, index, maxSum):
    base_nums = maxSum // n
    rest = maxSum % n

    def test(a):
        b = max(a - index, 0)
        res = (a + b) * (a - b + 1) / 2
        b = max(a - ((n - 1) - index), 0)
        res += (a + b) * (a - b + 1) / 2
        return res - a

    maxSum -= n
    left, right = 0, maxSum
    while left < right:
        mid = (left + right + 1) // 2
        if test(mid) <= maxSum:
            left = mid
        else:
            right = mid - 1
    return left + 1

if __name__ == '__main__':
    n = 6
    index = 1
    maxSum = 10
    print(maxValue(n, index, maxSum))
    # 3