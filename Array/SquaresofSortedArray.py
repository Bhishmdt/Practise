"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

def sortedSquares(nums):
    answer = []
    l, r = 0, len(nums) - 1
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            answer.append(nums[l] ** 2)
            l += 1
        else:
            answer.append(nums[r] ** 2)
            r -= 1
    return answer[::-1]

if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums))
    # Returns [0, 1, 9, 16, 100]

    nums = [-7, -3, 2, 3, 11]
    print(sortedSquares(nums))
    # Return [4, 9, 9, 49, 121]