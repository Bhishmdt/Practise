"""
Given a binary tree, check whether it is a mirror of itself.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isMirror(root):
    if not root:
        return True
    stack = [(root.left, root.right)]
    while stack:
        L, R = stack.pop()
        if not L and not R:
            continue
        if not L or not R or L.val != R.val:
            return False
        stack.append((L.left, R.right))
        stack.append((L.right, R.left))
    return True

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)
    
    print(isMirror(root))
    # True
    root.right.right = TreeNode(6)
    print(isMirror(root))
    # False