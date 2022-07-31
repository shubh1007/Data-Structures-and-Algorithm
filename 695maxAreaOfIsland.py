class Solution:
    def maxAreaOfIsland(self, grid):
        visited = set()
        def dfs(r,c):
            if r<0 or c<0 or r==len(grid) or c==len(grid[0]) or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return (1 + 
                    dfs(r+1, c) +
                    dfs(r-1, c) +
                    dfs(r, c+1) +
                    dfs(r, c-1) 
                    )
            
            
        ROWS, COLS = len(grid), len(grid[0])
        MAX = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    count = 1
                    count = dfs(r,c)
                    MAX = max(MAX, count)
        return MAX
        
        
        
        
        
        
        
sol = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
print(sol.maxAreaOfIsland(grid))