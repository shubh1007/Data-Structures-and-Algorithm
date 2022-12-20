class Solution:
    def uniquePathsIII(self, grid):
        hashMap = {}
        m, n = len(grid), len(grid[0])
        validCount = 0
        invalidCount = 0
        start = (0, 0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: start = (i, j)
                elif grid[i][j] == 0: validCount += 1
                elif grid[i][j] == -1: invalidCount += 1
                
        def traverse(i, j):
            if (i, j) in hashMap: return hashMap[(i, j)]
            if i < 0 or j < 0 or i == m or j == n: return 0
            if grid[i][j] == 2: 
                if validCount 
                return 1
            if grid[i][j] == -1: return 0
            if grid[i][j] == 1: return 1
            left = traverse(i, j - 1)
            right = traverse(i, j + 1)
            up = traverse(i - 1, j)
            down = traverse(i + 1, j)
            hashMap[(i, j)] = left + right + up + down
            validCount += 1
            return hashMap[(i, j)]
        return traverse(*start)

grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
sol = Solution()
res = sol.uniquePathsIII(grid)
print(res)

