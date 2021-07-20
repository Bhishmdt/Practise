"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
If there are no nodes with an even-valued grandparent, return 0.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumEvenGrandparent(root):
    def helper(root, p, g):
        even = g % 2
        if root:
            return helper(root.left, root.val, p) + helper(root.right, root.val, p) + root.val * (1 - even)
        else:
            return 0
    return helper(root, 1, 1)

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(5)
    print(sumEvenGrandparent(root))
    # Returns 13

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(5)
    print(sumEvenGrandparent(root))
    # Returns 0
