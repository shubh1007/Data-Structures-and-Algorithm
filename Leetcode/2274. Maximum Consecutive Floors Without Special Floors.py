class Solution:
    def maxConsecutive(self, bottom, top, special):
        special.sort()
        special = [bottom - 1] + special + [top + 1]
        res = 0
        for i in range(1, len(special)):
            res = max(res, special[i] - special[i - 1] - 1)
        return res

sol = Solution()
bottom = 2
top = 9
special = [4, 6]
res = sol.maxConsecutive(bottom, top, special)
print(res)