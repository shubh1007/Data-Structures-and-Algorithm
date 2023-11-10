class Solution:
    def maxProfit(self, prices):
        hashMap = {}
        n = len(prices)
        def dfs(i, buying):
            if i >= n: return 0
            if (i, buying) in hashMap: return hashMap[(i, buying)]
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                hashMap[(i, buying)] = max(buy, cooldown) 
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                hashMap[(i, buying)] = max(sell, cooldown) 
            return hashMap[(i, buying)]
        return dfs(0, True)
    
prices = [1, 2, 3, 0, 2]
sol = Solution()
res = sol.maxProfit(prices)
print(res)
        