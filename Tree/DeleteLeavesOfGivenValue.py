"""
Given a binary tree root and an integer target, delete all the leaf nodes with value target.
Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you can't).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def removeLeafNodes(root, target):
    if root.left:
        root.left = removeLeafNodes(root.left, target)
    if root.right:
        root.right = removeLeafNodes(root.right, target)
    if root.left is None and root.right is None and root.val == target:
        return None
    return root

COUNT = 5

def print2DUtil(root, space):
    if (root == None):
        return

    space += COUNT
    print2DUtil(root.right, space)
    for i in range(COUNT, space):
        print(end=" ")
    print(root.val)
    print2DUtil(root.left, space)

def print2D(root):
    print2DUtil(root, 0)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(2)
    target = 2

    print2D(removeLeafNodes(root, target))
    """
    Prints
    
              4
     3
1

    """