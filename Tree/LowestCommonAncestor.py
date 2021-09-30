"""
Given values of nodes n1 and n2 in a BST, find the lowest common ancestor. You may assume that both the values exist in th tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def LCA(root, n1, n2):

    while root:
        if root.val > n1 and root.val > n2:
            root = root.left
        elif root.val < n1 and root.val < n2:
            root = root.right
        else:
            return root.val

if __name__ == '__main__':
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)

    print(LCA(root, 10, 14))
    # 12
    print(LCA(root, 4, 14))
    # 8
    print(LCA(root, 10, 22))
    # 20
