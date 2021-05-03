"""
Find height of binary tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def heightTree(root):
    # Base case, when node is None
    if not root:
        return 0
    # Maximum height is root(1) + maximum of height of left and right trees.
    return max(heightTree(root.left), heightTree(root.right)) + 1
if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.left.right = TreeNode(12)
    root.left.left.right.right = TreeNode(15)
    root.right = TreeNode(20)
    root.right.left = TreeNode(2)

    print(heightTree(root))
    # Returns 5
