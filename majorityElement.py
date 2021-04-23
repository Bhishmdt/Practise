'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

def majorityElement(nums):
    # Consider first element as majority element
    current = nums[0]
    count = 0
    for i in range(len(nums)):
        # Increase count if number matches current majority element
        if nums[i] == current:
            count += 1
        # Decrease count if number does not match current majority element
        else:
            count -= 1
        # Change majority element if count is zero
        if count == 0:
            current = nums[i]
            count += 1
    # Net count of majority element will always be positive
    return current

if __name__ == '__main__':

    nums = [3, 2, 3]
    print(majorityElement(nums))
    # Returns 3

    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement(nums))
    # Returns 2