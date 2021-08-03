"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
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
    level = 1
    while stack:
        result.append([root.val for root in stack])
        temp = []
        for root in stack:
            if level % 2 == 0:
                if root.left:
                    temp.append(root.left)
                if root.right:
                    temp.append(root.right)
            else:
                if root.right:
                    temp.append(root.right)
                if root.right:
                    temp.append(root.left)

        stack = temp
        level += 1
    return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(2)
    print(levelOrder(root))
    # Returns [[1], [3, 2], [2, 4, 2]]