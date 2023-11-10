class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        grid = [[[-1 for i in range(maxMove)] for i in range(n)]for i in range(m)]
        def dfs(r,c, count):
            if (r<0 or c<0 or r==m or c==n): return 1
            if count < 0: return 0
            if grid[r][c][count] != -1: return grid[r][c][count]
            res = dfs(r-1, c, count - 1) + dfs(r+1, c, count - 1) + dfs(r, c+1, count - 1) + dfs(r, c-1, count - 1)
            res = res%1000000007
            grid[r][c][count] = res
            return res
        
        return dfs(startRow, startColumn, maxMove-1)



sol = Solution()
m, n = 2, 2
maxMove = 2
startRow, startColumn = 0, 0        
print(sol.findPaths(m, n, maxMove, startRow, startColumn))