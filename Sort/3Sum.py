"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
def threeSum(nums):
    if len(nums) < 3:
        return []
    result = []
    # Sort the numbers
    nums.sort()
    for i in range(len(nums) - 2):
        # Check repetition of first number
        if i > 0 and nums[i] == nums[i -1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            # If sum is less than zero move left pointer to right, if gretaer than zero move right pointer to left
            if nums[i] + nums[l] + nums[r] == 0:
                result.append([nums[i], nums[l], nums[r]])
                # Skip if numbers are repeated
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1
    return result

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
    # Returns [[-1, -1, 2], [-1, 0, 1]]
