class Solution:
    def minDeletionSize(self, strs):
        m, n = len(strs), len(strs[0])
        count = 0
        for col in range(n):
            for row in range(1, m):
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    break
        return count

sol = Solution()
strs = ["cba","daf","ghi"]
res = sol.minDeletionSize(strs)
print(res)