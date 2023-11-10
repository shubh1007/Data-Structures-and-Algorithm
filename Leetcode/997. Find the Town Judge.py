from collections import defaultdict

class Solution:
    def findJudge(self, n, trust):
        otherTrust = defaultdict(int)
        yourTrust = defaultdict(int)
        for x, y in trust:
            yourTrust[x] += 1
            otherTrust[y] += 1
        for i in range(1, n + 1):
            if otherTrust[i] == n - 1 and yourTrust[i] == 0:
                return i
        return -1

n = 3
trust = [[1,3],[2,3]]
sol = Solution()
res = sol.findJudge(n, trust)
print(res)

            
