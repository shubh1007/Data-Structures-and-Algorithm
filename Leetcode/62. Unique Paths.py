class Solution:
    def uniquePaths(self, m, n):
        hashMap = {}
        def traverse(i, j):
            if (i, j) in hashMap: return hashMap[(i, j)]
            if i == m or j == n: return 0
            if i == m - 1 and j == n - 1: return 1
            right = traverse(i, j + 1)
            down = traverse(i + 1, j)
            hashMap[(i, j)] = right + down
            return hashMap[(i, j)]
        return traverse(0, 0)

m = 3
n = 7
sol = Solution()
res = sol.uniquePaths(m, n)
print(res)

