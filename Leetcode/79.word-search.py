class Solution(object):
    def exist(self, board, word):
 
        if not board or not board[0] or not word: return False
        
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                # check if word exists
                if self._dfs(board, word, r, c, rows, cols, []): 
                    return True
        
        return False
   def _dfs(self, board, word, r, c, rows, cols, visited):

        if not word: return True
        
        if r < 0 or r >= rows or c < 0 or c >= cols or \
            word[0] != board[r][c] or (r, c) in visited:
            return False
        
        visited.append((r, c))
        nxt = self._dfs(board, word[1:], r - 1, c, rows, cols, visited) or \
                self._dfs(board, word[1:], r + 1, c, rows, cols, visited) or \
                self._dfs(board, word[1:], r, c + 1, rows, cols, visited) or \
                self._dfs(board, word[1:], r, c - 1, rows, cols, visited)
        if not nxt: visited.pop()   # reset visited
        return nxt        
