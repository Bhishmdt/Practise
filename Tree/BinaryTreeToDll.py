"""
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place.
The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL.
The order of nodes in DLL must be same as Inorder of the given Binary Tree.
The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.
"""

class DLLNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def TreeToDll(root):

    sentinal = dummy = DLLNode()
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
                temp = DLLNode(current.val)
                dummy.next = temp
                temp.prev = dummy
                dummy = temp
                current = current.right
        else:
            temp = DLLNode(current.val)
            dummy.next = temp
            temp.prev = dummy
            dummy = temp
            current = current.right
    sentinal.next.prev = None
    return sentinal.next

def printDLL(root):

    curr = root
    while curr:
        
        print('Data =', curr.val, end=" ")
        if curr.next:
            print('next =', curr.next.val, end=" ")
        else:
            print("next = None", end=" ")
        if curr.prev:
            print('prev =', curr.prev.val)
        else:
            print('prev = None',)
        curr = curr.next

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
    printDLL(TreeToDll(root))
    

