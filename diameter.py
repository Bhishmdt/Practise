"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    # Find height of left and right tree
    def height(root):
        global d
        if not root:
            return 0
        L = height(root.left)
        R = height(root.right)
        # Store the maximum in d
        d = max(d, L + R + 1)
        return 1 + max(L, R)

    height(root)
    # Return number of nodes - 1
    return d - 1

if __name__ == '__main__':
    d = 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.left.left = TreeNode(7)
    root.left.right.left.left.left = TreeNode(8)
    root.left.right.right = TreeNode(9)
    root.left.right.right.right = TreeNode(10)
    print(diameterOfBinaryTree(root))
    # Returns 6
    root.left.right.left.left.left.left = TreeNode(20)
    root.left.right.right.right.right = TreeNode(11)
    root.left.right.right.right.right.right = TreeNode(12)
    print(diameterOfBinaryTree(root))
    # Returns 8