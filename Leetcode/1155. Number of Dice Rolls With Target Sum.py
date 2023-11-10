class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        mod = 10**9+7
        dp = [[0]*(target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        if target < 1 or target > n*k: return 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for m in range(j, target + 1):
                    dp[i][m] = (dp[i][m] + dp[i-1][m-j]) % mod
        return dp[-1][-1]
