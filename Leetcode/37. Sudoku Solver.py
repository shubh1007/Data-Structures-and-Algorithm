class Solution:
    def solveSudoku(self, board):
        n = len(board)
        def solve():
            for i in range(n):
                for j in range(n):
                    if board[i][j] == ".":
                        for char in range(1, 10):
                            if isValid(i, j, str(char)):
                                board[i][j] = str(char)
                                if solve():
                                    return True
                                board[i][j] = "."
                        return False
            return True  

        def isValid(i, j, c):
            for row in range(n): 
                if board[row][j] == c: return False
            for col in range(n):
                if board[i][col] == c: return False
            for row in range((i//3)*3, (i//3)*3 + 3):
                for col in range((j//3)*3, (j//3)*3 + 3):
                    if board[row][col] == c:
                        return False
            return True
        solve()                


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

sol = Solution()
sol.solveSudoku(board)
for i in board:
    for j in i:
        print(j, end = " ")
    print()