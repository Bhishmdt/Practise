"""
Serialization is to store a tree in an array so that it can be later restored and Deserialization is reading tree back from the array.
Now your task is to complete the function serialize which stores the tree into an array A[ ] and deSerialize which deserializes the array to tree and returns it.
Note: The structure of tree must be maintained.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Serialize(root):
    output = []
    def helper(node):
        if node:
            output.append(str(node.val))
            helper(node.left)
            helper(node.right)
        else:
            output.append('/')

    helper(root)
    return ' '.join(output)

def deserialize(S):
    def helper():
        s = next(S)
        if s == '/':
            return None
        node = TreeNode(int(s))
        node.left = helper()
        node.right = helper()
        return node

    S = iter(S.split())
    return helper()

def print2DUtil(root, space):
    if (root == None):
        return

    space += 5
    print2DUtil(root.right, space)
    for i in range(5, space):
        print(end=" ")
    print(root.val)
    print2DUtil(root.left, space)

def print2D(root):
    print2DUtil(root, 0)

if __name__ == '__main__':
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)
    
    data = Serialize(root)
    print(data)
    print2D(deserialize(data))
    
    