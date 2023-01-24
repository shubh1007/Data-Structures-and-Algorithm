from collections import deque
class Solution:
    def snakesAndLadders(self, board):
        # Get the length of board
        n = len(board)
        # reverse the board so that it will be easier for us to access the board elements
        # |  7  |  8  |  9  |                |  1  |  2  |  3  |
        # |  6  |  5  |  4  |       =>       |  6  |  5  |  4  |
        # |  1  |  2  |  3  |                |  7  |  8  |  9  |
        board.reverse()
        def numToPos(square):
            # This method will deduce the position of the given square
            # Let us say we want to get the position of square 5 
            # then the row's index will be (square - 1) // length of board
            # (5 - 1) // 3 = 4 // 3 = 1
            # (4 - 1) // 3 = 3 // 3 = 1
            row = (square - 1) // n
            # Similarly col's index will be (square - 1) % length of board
            col = (square - 1) % n
            # Since the board is arranged in Boustrophedon style, So we will have to take care of col sequence
            # it is observed that in the odd row index col must be reversed. 
            # So we flip the values in the odd row for all the board[odd rows][col]
            if row % 2:
                # this is the logic for flipping the col values of odd rows
                col = n - 1 - col
            return [row, col]
        Q = deque()
        # We do BFS to get to the final destination
        Q.append([1, 0])
        visited = set()
        while Q:
            
            currSquare, currMoves = Q.popleft()
            for i in range(1, 7):
                nextSquare = currSquare + i
                row, col = numToPos(nextSquare)
                if board[row][col] != -1:
                    nextSquare = board[row][col]
                if nextSquare == n * n:
                    return currMoves + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    Q.append([nextSquare, currMoves + 1])
        return -1 































# from collections import deque

# class Solution:
#     def snakesAndLadders(self, board: list[list[int]]) -> int:
#         n = len(board)
#         board.reverse()
#         def numToPos(square):
#             row =  (square - 1) // n
#             col = (square - 1) % n
#             if row % 2:
#                 col = n - 1 - col
#             return [row, col]
        
#         Q = deque()
#         visited = set()
#         Q.append([1, 0])
#         while Q:
#             square, moves = Q.popleft()
#             for i in range(1, 7):
#                 nextSquare = square + i
#                 row, col = numToPos(nextSquare)
#                 if board[row][col] != -1:
#                     nextSquare = board[row][col]
#                 if nextSquare == n * n:
#                     return moves + 1
#                 if nextSquare not in visited:
#                     visited.add(nextSquare)
#                     Q.append([nextSquare, moves + 1])
#         return - 1




        
