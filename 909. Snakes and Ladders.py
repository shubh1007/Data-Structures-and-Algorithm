from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        board.reverse()
        def numToPos(square):
            row =  (square - 1) // n
            col = (square - 1) % n
            if row % 2:
                col = n - 1 - col
            return [row, col]
        
        Q = deque()
        visited = set()
        Q.append([1, 0])
        while Q:
            square, moves = Q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                row, col = numToPos(nextSquare)
                if board[row][col] != -1:
                    nextSquare = board[row][col]
                if nextSquare == n * n:
                    return moves + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    Q.append([nextSquare, moves + 1])
        return - 1



        
