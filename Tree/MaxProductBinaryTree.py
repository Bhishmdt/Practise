"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxProduct(root):
    sumarray = []

    def helper(root):
        if not root:
            return 0
        S = root.val + helper(root.right) + helper(root.left)
        sumarray.append(S)
        return S

    total = helper(root)
    result = 0
    for e in sumarray:
        result = max(result, e * (total - e))
    return result % (10 ** 9 + 7)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(5)
    print(maxProduct(root))
    # Return 112