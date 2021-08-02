"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    if p and q:
        return p.val == q.val and isSameTree(p.right, q.right) and isSameTree(p.left, q.left)
    return p is q


if __name__ == '__main__':
    root1 = TreeNode(2)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.right.left = TreeNode(9)

    root2 = TreeNode(2)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.right.left = TreeNode(9)

    print(isSameTree(root2, root1))
    # Returns True