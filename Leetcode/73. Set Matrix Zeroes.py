from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeroes = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes.append([i, j])
        for row, col in zeroes:
            for c in range(n):
                matrix[row][c] = 0
            for r in range(m):
                matrix[r][col] = 0
        
