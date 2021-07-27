"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    d = collections.defaultdict(int)

    def helper(root, depth, ans, d):
        if not root:
            return
        if d[depth] == 0:
            ans.append(root.val)
            d[depth] = 1
        helper(root.right, depth + 1, ans, d)
        helper(root.left, depth + 1, ans, d)

    ans = []
    helper(root, 0, ans, d)
    return ans

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(2)
    print(rightSideView(root))
    # Returns [1, 3, 4]

    root = TreeNode(11)
    root.left = TreeNode(5)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(10)
    print(rightSideView(root))
    # Returns [11, 7, 10]

    root = TreeNode(11)
    root.left = TreeNode(5)
    print(rightSideView(root))
    # Returns [11, 5]