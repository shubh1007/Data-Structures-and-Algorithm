from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hs = set()
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and (r, c) not in hs:
                hs.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        for row in range(m):
            dfs(row, 0)
            dfs(row, n - 1)
        for col in range(1, n - 1):
            dfs(0, col)
            dfs(m - 1, col)
        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in hs:
                    res += 1
        return res

if __name__ == "__main__":
    print(Solution().numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
