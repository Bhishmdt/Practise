"""
Check if two trees are identical or not.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isIdenticalTree(a, b):
    if a and b:
        # Check if value of root is same and the left and right trees are identical.
        return a.val == b.val and isIdenticalTree(a.left, b.left) and isIdenticalTree(a.right, b.right)
    # check if both are a and b are none. 
    return a is b
if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.left = TreeNode(4)
    a.left.right = TreeNode(5)

    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(3)
    b.left.left = TreeNode(4)
    b.left.right = TreeNode(5)

    print(isIdenticalTree(a, b))
    # Returns True

    c = TreeNode(1)
    c.left = TreeNode(2)
    c.right = TreeNode(3)
    c.left.left = TreeNode(4)
    c.left.right = TreeNode(5)
    c.left.right.right = TreeNode(6)

    print(isIdenticalTree(a, c))
    # Returns False