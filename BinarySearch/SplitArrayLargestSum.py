"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.
"""

def splitArray(nums, m):
    def check(sum):
        splits = 1
        subarraysum = 0
        for num in nums:
            subarraysum += num
            if subarraysum > sum:
                subarraysum = num
                splits += 1
                if splits > m:
                    return False
        return True

    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    print(splitArray(nums, m))
    # Returns 18