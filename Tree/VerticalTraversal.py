"""
Print vertical traversal of tree.
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printVerticalTraversal(root):
    d = {}
    q = deque()
    q.append([root, 0])

    while q:
        node, pos = q.popleft()
        d[pos] = d.get(pos, []) + [node.val]

        if node.left:
            q.append([node.left, pos - 1])
        if node.right:
            q.append([node.right, pos + 1])

    d = dict(sorted(d.items(), key=lambda item: item[0]))
    for k, v in d.items():
        for e in v:
            print(e, end=" ")


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.left.right = TreeNode(8)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(9)

    printVerticalTraversal(root)
    # 4 2 1 5 6 3 8 7 9