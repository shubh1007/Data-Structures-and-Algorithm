class Solution:
    def kInversePairs(self, n, k):
        dp = [[-1 for i in range(1001)] for i in range(1001)]
        def helper(n,k):
            if n == 0: return 0
            if k == 0: return 1
            if dp[n][k] != -1: return dp[n][k]
            count = 0
            for i in range(min(k, n-1)):
                count = (count + helper(n-1, k-i))%1000000007
            dp[n][k] = count
            return count
        return helper(n,k)
    

sol = Solution()
n = 3
k = 0
print(sol.kInversePairs(n, k))