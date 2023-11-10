class Solution:
    def numTilings(self, n):
        if n < 3: return n
        dp = [0] * (4)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4, n + 1):
            temp = 2 * dp[3] + dp[1]
            dp.pop(0)
            dp.append(temp)

        return dp[-1] % (10**9 + 7)
    
sol =  Solution()
n = 100
res = sol.numTilings(n)
print(res)

