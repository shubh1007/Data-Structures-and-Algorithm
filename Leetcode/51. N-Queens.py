class Solution:
    def nQueens(self, n):
        cols = set()
        posDiag = set()
        negDiag = set()
        grid = [["." for _ in range(n)] for _ in range(n)]
        result = []
        def track(row):
            if row == n:
                copy = ["".join(r) for r in grid]
                result.append(copy)
                return
            for col in range(n):
                if col in cols or row + col in posDiag or row - col in negDiag:
                    continue
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                grid[row][col] = "Q"
                track(row + 1)
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                grid[row][col] = "."
        track(0)
        return result

sol = Solution()
n = 4
result = sol.nQueens(n)
for i in result:
    for j in i:
        print(j)
    print()