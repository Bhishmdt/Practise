"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two adjacent nodes in the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root):
    if not root:
        return float('inf')

    L = float('inf')
    R = float('inf')

    if root.left:
        L = abs(root.val - root.left.val)
    if root.right:
        R = abs(root.val - root.right.val)

    return min(min(L, R), getMinimumDifference(root.left), getMinimumDifference(root.right))

if __name__ == '__main__':
    root = TreeNode(11)
    root.left = TreeNode(5)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(10)

    print(getMinimumDifference(root))
    # Returns 4