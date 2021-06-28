"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root):
    A = []

    def inorder(root):
        if not root:
            return A
        inorder(root.left)
        A.append(root.val)
        inorder(root.right)

    inorder(root)
    mindiff = float('inf')
    for i in range(1, len(A)):
        mindiff = min(abs(A[i] - A[i - 1]), mindiff)
    return mindiff

if __name__ == '__main__':
    root = TreeNode(11)
    root.left = TreeNode(5)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(10)

    print(getMinimumDifference(root))
    # Returns 1
