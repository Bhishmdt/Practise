"""
Given an array of integers arr and an integer target.
You have to find two non-overlapping sub-arrays of arr each with a sum equal target.
There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.
Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.
"""


def minSumOfLengths(arr, target):
    result_i = [float('inf')] * len(arr)
    result = float('inf')
    currsum = 0
    left = 0
    for right in range(len(arr)):
        currsum += arr[right]
        #Move left to position where currsum is less than target
        while currsum > target and left <= right:
            currsum -= arr[left]
            left += 1
        if currsum == target:
            result = min(result, result_i[left - 1] + right - left + 1)
            result_i[right] = min(result_i[right - 1], right - left + 1)
        else:
            result_i[right] = result_i[right - 1]

    if result == float('inf'):
        return -1
    return result

if __name__ == '__main__':
    arr = [3, 1, 1, 1, 5, 1, 2, 1]
    target = 3
    print(minSumOfLengths(arr, target))
