"""
Print bottom view of tree from left to right.
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getBottomView(root):
    d = {}
    q = deque()
    q.append([root, 0])

    while q:
        node, pos = q.popleft()
        d[pos] = node.val

        if node.left:
            q.append([node.left, pos - 1])
        if node.right:
            q.append([node.right, pos + 1])

    d = dict(sorted(d.items(), key=lambda item: item[0]))
    for k, v in d.items():
        print(v, end=" ")
        
if __name__ == '__main__':
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(5)    
    root.left.right = TreeNode(3)
    root.left.right.left = TreeNode(10)
    root.right.left = TreeNode(4)
    root.right.left.right = TreeNode(14)
    root.right.right = TreeNode(25)
    getBottomView(root)
    # 5 10 4 14 25 


