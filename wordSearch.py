"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

def exist(board, word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False

def dfs(board, i, j, word):
    # If all words are found, return True
    if len(word) == 0:
        return True
    # Check out of bounds and if word[0] is present at position i, j
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
        return False
    temp = board[i][j]
    # Mark current word as visited
    board[i][j] = "$"
    # Search for next word in all four directions
    result = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
    board[i][j] = temp
    return result

if __name__ == '__main__':
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "SEE"
    print(exist(board, word))
    # Returns True
    word = "ABA"
    print(exist(board, word))
    # Returns False
