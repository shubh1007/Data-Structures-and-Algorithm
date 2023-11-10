class Solution:
    def uniquePathsIII(self, grid):
        self.res = 0
        m, n = len(grid), len(grid[0])
        start, end = 0, 0
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] != -1:
                    count += 1

        def traverse(i, j, COUNT):
            if (i < 0 or j < 0 or i == m or j == n):
                return
            elif (i, j) == end:
                if COUNT == count:
                    self.res += 1
                return
            elif grid[i][j] == -1:
                return
            # print((i, j), COUNT)
            grid[i][j] = -1
            traverse(i, j - 1, COUNT + 1)
            traverse(i, j + 1, COUNT + 1)
            traverse(i - 1, j, COUNT + 1)
            traverse(i + 1, j, COUNT + 1)
            grid[i][j] = 0

        traverse(start[0], start[1], 1)
        return self.res


grid = [[0,1],[2,0]]
sol = Solution()
res = sol.uniquePathsIII(grid)
print(res)
