"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
"""

def subarraySum(nums, k):
    # Initialize sum of zero by 1
    count, i, currsum, result = {0: 1}, 0, 0, 0

    while i <= len(nums) - 1:
        # Find cumulative sum
        currsum += nums[i]
        # If cumulative sum minus target in keys, add value to result
        result += count.get(currsum - k, 0)
        # Store currsum as key and number of times it appeared as value
        count[currsum] = count.get(currsum, 0) + 1
        i += 1

    return result

if __name__ == '__main__':
    print(subarraySum([0, 1, 1, 2, 3, -1, 5], 2))
    # Cumulative sum ([0, 1, 2, 4, 7, 6, 11])
    # Returns 4 ([0, 1, 1], [1, 1], [2], [3, -1])

    print(subarraySum([1, 1, 1, 1], 3))
    # Returns 2 ([1, 1, 1] * 2)
