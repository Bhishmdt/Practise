"""

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def widthOfBinaryTree(root):
    width = 0
    level_nodes = [(root, 1)]
    while level_nodes:
        width = max(width, level_nodes[-1][1] - level_nodes[0][1] + 1)
        next_level = []
        for node, index in level_nodes:
            if node.left:
                next_level.append((node.left, 2 * index))
            if node.right:
                next_level.append((node.right, 2 * index + 1))
            level_nodes = next_level
    return width

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(5)
    print(widthOfBinaryTree(root))
    # Returns 2