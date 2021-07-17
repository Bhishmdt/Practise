"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""


def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    if not board:
        return

    def dfs(board, i, j):
        if len(board) > i >= 0 and len(board[0]) > j >= 0 and board[i][j] == 'O':
            board[i][j] = 'S'
            dfs(board, i + 1, j)
            dfs(board, i, j + 1)
            dfs(board, i - 1, j)
            dfs(board, i, j - 1)

    for i in (0, len(board) - 1):
        for j in range(len(board[0])):
            dfs(board, i, j)

    for i in range(len(board)):
        for j in (0, len(board[0]) - 1):
            dfs(board, i, j)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'S':
                board[i][j] = 'O'
    print(board)

if __name__ == '__main__':
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    solve(board)
    """
    Prints
    [['X', 'X', 'X', 'X'], 
    ['X', 'X', 'X', 'X'], 
    ['X', 'X', 'X', 'X'], 
    ['X', 'O', 'X', 'X']]
    """