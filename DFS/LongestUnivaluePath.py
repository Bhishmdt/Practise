"""
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestUnivaluePath(root):
    maximum = [0]

    def helper(root):
        if not root:
            return 0
        right = helper(root.right)
        left = helper(root.left)
        if root.left and root.left.val == root.val:
            left += 1
        else:
            left = 0

        if root.right and root.right.val == root.val:
            right += 1
        else:
            right = 0
        maximum[0] = max(maximum[0], left + right)
        return max(left, right)

    helper(root)
    return maximum[0]

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(5)
    print(longestUnivaluePath(root))
    # Returns 2
