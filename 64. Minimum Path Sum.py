from sys import maxsize

class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = [[float("inf") for _ in range(n + 1)] for _ in range(m + 1)]
        res[m][n - 1] = 0
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                res[row][col] = grid[row][col] + min(res[row + 1][col], res[row][col + 1])
        return res[0][0]
        
sol = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
result = sol.minPathSum(grid)
print(result)
    
