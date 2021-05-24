"""
Implementation of dictionary
"""

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie(object):
    # Initialize root node
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for char in word:
            # Traverse till one of the children of present node contain the char, or create new node
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def dfs(self, node, pre):
        if node.is_end:
            self.output.append((pre + node.char))
        for child in node.children.values():
            self.dfs(child, pre + node.char)

    def search(self, x):
        node = self.root
        # Traverse till the node of last char of searched word
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # If the word is not found, return []
                return []
        self.output = []
        # Dfs
        self.dfs(node, x[:-1])
        return self.output

if __name__ == '__main__':
    tr = Trie()
    tr.insert("here")
    tr.insert("hear")
    tr.insert("he")
    tr.insert("hello")
    tr.insert("how ")
    tr.insert("her")
    
    print(tr.search("he"))
    # Returns ['he', 'her', 'here', 'hear', 'hello']