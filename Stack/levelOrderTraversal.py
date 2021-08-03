"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []
    stack = [root]
    result = []

    while stack:
        result.append([root.val for root in stack])
        temp = []
        for root in stack:
            if root.left:
                temp.append(root.left)
            if root.right:
                temp.append(root.right)

        stack = temp
    return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(2)
    print(levelOrder(root))
    # Returns [[1], [2, 3], [2, 2, 4]]