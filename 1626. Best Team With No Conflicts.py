class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        v = [] 
        n = len(scores)
        for i in range(n):
            v.append((-ages[i], -scores[i]))
        v.sort()
        dp = [0 for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i, -1, -1):
                if (-v[i][1] <= -v[j][1]):
                    dp[i] = max(dp[i], dp[j] - v[i][1])
            ans = max(ans, dp[i])
        return ans
    
scores = [1,3,5,10,15]
ages = [1,2,3,4,5]
sol = Solution()
res = sol.bestTeamScore(scores, ages)
print(res)