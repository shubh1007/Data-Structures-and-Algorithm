class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n = len(grid)
        m = len(grid[0])
        q = []
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 1):
                    q.append((i, j))
        if not q: return -1
        ans = 0
        while q:
            x, y = q.pop(0)
            for direction in range(4):
                tx = x + dx[direction]
                ty = y + dy[direction]
                if (tx >= 0 and tx < n and ty >= 0 and ty < m and grid[tx][ty] ==0):
                    grid[tx][ty] = grid[x][y] + 1
                    ans = max(grid[tx][ty], ans)
                    q.append((tx, ty))
        return ans - 1
