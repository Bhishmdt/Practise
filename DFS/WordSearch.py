"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

def exist(board, word):
    if not board:
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, word, i, j) == True:
                return True
    return False

def dfs(board, word, i, j):
    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
        return False
    tmp = board[i][j]
    board[i][j] = '#'

    result = dfs(board, word[1:], i + 1, j) or dfs(board, word[1:], i, j + 1) or dfs(board, word[1:], i - 1, j) or dfs(board, word[1:], i, j - 1)

    board[i][j] = tmp
    return result

if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(exist(board, word))
    # Returns True

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    print(exist(board, word))
    # Returns False