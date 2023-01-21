class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        n = len(s)
        if len(s) > 12: return []
        def helper(i, dots, curIP):
            if dots == 4 and i == n:
                res.append(curIP[:-1])
                return
            if dots > 4: return 
            for j in range(i, min(i + 3, n)):
                if int(s[i: j + 1]) <= 255 and (i == j or s[i] != "0"):
                    helper(j + 1, dots + 1, curIP + s[i: j + 1] + ".")
        helper(0, 0, "")
        return res

s = "25525511135"
sol = Solution()
res = sol.restoreIpAddresses(s)
print(res)






        