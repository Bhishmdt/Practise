"""
Given the root of a binary tree, return all root-to-leaf paths in any order.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    if not root:
        return []
    result = []
    dfs(root, "", result)
    return result

def dfs(root, path, result):
    # If leaf node, append path to result
    if not root.left and not root.right:
        result.append(path + str(root.val))
    if root.left:
        dfs(root.left, path + str(root.val) + "->", result)
    if root.right:
        dfs(root.right, path + str(root.val) + "->", result)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(binaryTreePaths(root))
    # Returns ['1->2->4', '1->2->5', '1->3']