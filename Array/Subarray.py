"""
Print all subarrays of an array.
"""
def subarrays(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            print(nums[i:j])

if __name__ == '__main__':
    nums = [1,2,3]
    subarrays(nums)
    # Returns [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]