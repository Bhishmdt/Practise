"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    if not root:
        return True

    return abs(HeightOfTree(root.left) - HeightOfTree(root.right)) < 2 and isBalanced(root.left) and isBalanced(root.right)

def HeightOfTree(root):
    if not root:
        return True

    return 1 + max(HeightOfTree(root.left), HeightOfTree(root.right))

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(isBalanced(root))
    # Returns True

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    print(isBalanced(root))
    # Returns False

