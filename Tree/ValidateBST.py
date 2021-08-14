"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def helper(root, small, big):
        if not root:
            return True
        if root.val <= small or root.val >= big:
            return False
        return helper(root.left, small, root.val) and helper(root.right, root.val, big)

    return helper(root, -float('inf'), float('inf'))

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    
    print(isValidBST(root))
    # Returns False

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    print(isValidBST(root))
    # Returns True