"""
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

    For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

    Each element of nums is in exactly one pair, and
    The maximum pair sum is minimized.

Return the minimized maximum pair sum after optimally pairing up the elements.
"""


def minPairSum(nums):
    # to minimize, we need to take pairs of min and max elements
    nums.sort()
    minmaxsum = -float('inf')
    for i in range(len(nums) // 2):
        minmaxsum = max(minmaxsum, nums[i] + nums[-1 - i])

    return minmaxsum

if __name__ == '__main__':
    nums = [3, 5, 4, 2, 4, 6]
    print(minPairSum(nums))
    # Returns 8