"""
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.
"""
import heapq

def maxResult(nums, k):
    heap = [(-nums[0], 0)]
    result = nums[0]
    for i in range(1, len(nums)):
        while heap[0][1] < i - k:
            heapq.heappop(heap)
        result = nums[i] - heap[0][0]
        heapq.heappush(heap, (-result, i))

    return result

if __name__ == '__main__':
    nums = [1, -1, -2, 4, -7, 3]
    k = 2
    print(maxResult(nums, k))
    # Returns 7

    nums = [10, -5, -2, 4, 0, 3]
    k = 3
    print(maxResult(nums, k))
    # Returns 17

    nums = [1, -5, -20, 4, -1, 3, -6, -3]
    k = 2
    print(maxResult(nums, k))
    # Returns 0