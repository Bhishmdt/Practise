"""
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root):
    cur, node, cands = root, TreeNode(-float("inf")), []
    while cur:
        if cur.left:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            if not pre.right:
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                if cur.val < node.val:
                    cands += [node, cur]
                node = cur
                cur = cur.right
        else:
            if cur.val < node.val:
                cands += [node, cur]
            node = cur
            cur = cur.right

    cands[0].val, cands[-1].val = cands[-1].val, cands[0].val

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    recoverTree(root)
    print(root.val)
    # Returns 2