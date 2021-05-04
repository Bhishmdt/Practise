"""
Convert Tree to its mirror image
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    
def mirrorTree(root):
    if root:
        root.left, root.right = mirrorTree(root.right), mirrorTree(root.left)
        return root

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    inorder(root)
    # Prints 4 2 5 1 3

    print("\n")

    mirrorTree(root)
    inorder(root)
    # Prints 3 1 5 2 4

    
    