from sys import maxsize

class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in grid:
            i.append(float("inf"))
        grid.append([float("inf") for _ in range(n + 1)])
        grid[m][n - 1] = 0
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                grid[row][col] = grid[row][col] + min(grid[row + 1][col], grid[row][col + 1])
        return grid[0][0]
        
sol = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
result = sol.minPathSum(grid)
print(result)
    
