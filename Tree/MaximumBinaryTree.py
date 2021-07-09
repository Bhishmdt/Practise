"""
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

    Create a root node whose value is the maximum value in nums.
    Recursively build the left subtree on the subarray prefix to the left of the maximum value.
    Recursively build the right subtree on the subarray suffix to the right of the maximum value.

Return the maximum binary tree built from nums.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    root = TreeNode(max(nums))
    root.left = constructMaximumBinaryTree(nums[:nums.index(max(nums))])
    if nums.index(max(nums)) < len(nums) - 1:
        root.right = constructMaximumBinaryTree(nums[nums.index(max(nums)) + 1:])
    else:
        root.right = None
    return root

COUNT = 5

def print2DUtil(root, space):
    if (root == None):
        return

    space += COUNT
    print2DUtil(root.right, space)
    for i in range(COUNT, space):
        print(end=" ")
    print(root.val)
    print2DUtil(root.left, space)

def print2D(root):
    print2DUtil(root, 0)

if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    print2D(constructMaximumBinaryTree(nums))
    """
    Returns 
    5
          0
6
               1
          2
    3
    """