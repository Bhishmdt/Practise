""""
Given a binary tree and two nodes, x and y, find the lowest common ancestor (LCA) of x and y in it.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def LCA(root, x, y):
    # Return root if root is x, y or None
    if root in (None, x, y):
        return root
    left = LCA(root.left, x, y)
    right = LCA(root.right, x, y)
    # If both left and right have non None values, return root
    if left and right:
        return root
    # Else return non None value
    else:
        return left or right

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.right = TreeNode(7)
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(9)

    x = root.left
    y = root.right.right
    print(LCA(root, x, y).val)
    # Returns 1

    x = root.left.left
    y = root.left.right.right
    print(LCA(root, x, y).val)
    # Returns 2

    x = root.right
    y = root.right.right.left
    print(LCA(root, x, y).val)
    # Returns 7
