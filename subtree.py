"""
Check if one tree is subtree of another tree
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

def checkSubtree(t, s):
    # if t and s are identical, return True
    if isIdenticalTree(t, s):
        return True
    if not t:
        return False
    # If any of the subtrees of t are match of s, return True or else False
    return checkSubtree(t.left, s) or checkSubtree(t.right, s)

if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.left = TreeNode(4)
    a.left.right = TreeNode(5)
    b = TreeNode(2)
    b.left = TreeNode(4)
    b.right = TreeNode(5)
    print(checkSubtree(a, b))
    # Returns True

    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.left = TreeNode(4)
    a.left.right = TreeNode(5)
    b = TreeNode(2)
    b.left = TreeNode(3)
    b.right = TreeNode(5)
    print(checkSubtree(a, b))
    # Returns False
