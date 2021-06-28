"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.
A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    result = []

    def dfs(root, targetSum, result, path):
        if root:
            if not root.left and not root.right and targetSum == root.val:
                path.append(root.val)
                result.append(path)
            dfs(root.left, targetSum - root.val, result, path + [root.val])
            dfs(root.right, targetSum - root.val, result, path + [root.val])

    dfs(root, targetSum, result, [])
    return result

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    
    print(pathSum(root, 22))
    # Returns [[5, 4, 11, 2], [5, 8, 4, 5]]
