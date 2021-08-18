"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []
    result = []
    level = 0
    level_nodes = [root]
    while level_nodes:
        l = len(level_nodes)
        curr = []
        for i in range(l):
            if level % 2 == 0:
                node = level_nodes.pop(0)
                curr.append(node.val)
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
            else:
                node = level_nodes.pop()
                curr.append(node.val)
                if node.right:
                    level_nodes.insert(0, node.right)
                if node.left:
                    level_nodes.insert(0, node.left)
        result.append(curr)
        level += 1
    return result

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.left.right = TreeNode(5)
    print(zigzagLevelOrder(root))

    # [[3], [4, 1], [5, 2]]