class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        for row in range(N):
            for col in range(N):
                if board[row][col] != ".":
                    for c in range(N):
                        if board[row][c] == board[row][col] and c != col:
                            return False
                    for r in range(N):
                        if board[r][col] == board[row][col] and r != row:
                            return False
                    for r in range((row//3)*3, (row//3)*3 + 3):
                        for c in range((col//3)*3, (col//3)*3 + 3):
                            if board[r][c] == board[row][col] and r != row and c != col:
                                return False
        return True
                        
                
                
    
