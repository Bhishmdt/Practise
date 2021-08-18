"""
Inorder traversal without using additional memory.
"""
class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = None
        self.left = None
        
def MorrisTraversal(root):
    current = root
    while current:
        if current.left:
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right
            if not pre.right:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                print(current.val)
                current = current.right
        else:
            print(current.val)
            current = current.right

if __name__ == '__main__':
    root = TreeNode(11)
    root.left = TreeNode(5)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(10)
    MorrisTraversal(root)