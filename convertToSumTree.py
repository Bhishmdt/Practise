"""
Given a binary tree, in-place convert it into its sum tree. Each node's value is equal to the sum of all elements
present in its left and right subtree in a sum tree. Consider the value of an empty node as 0.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertSumTree(root):
    # Base case
    if not root:
        return 0

    L = convertSumTree(root.left)
    R = convertSumTree(root.right)
    # Store current value of root node
    old = root.val
    # root val is sum of left and right
    root.val = L + R
    # Return sum of new root val + old val
    return root.val + old

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    
    convertSumTree(root)
    inorder(root)
    # Returns 4 0 35 0 15 0 26 0
    

