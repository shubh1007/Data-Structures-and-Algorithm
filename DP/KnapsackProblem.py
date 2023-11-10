class Solution:
    def knapsack(self, values, weights, W, n):
        if (W == 0 or n == 0): return 0
        if weights[n - 1] > W:
            return self.knapsack(values, weights, W, n - 1)
        else:
            return max(values[n - 1] + self.knapsack(values, weights, W - weights[n - 1], n - 1),
                       self.knapsack(values, weights, W, n - 1))
    
    def knapsackMemo(self, values, weights, W, n):
        self.memo = [[-1 for i in range(W + 1)] for j in range(n + 1)]
        def helper(values, weights, W, n):
            if (W == 0 or n == 0): return 0
            if self.memo[n][W] != -1:
                return self.memo[n][W]
            if weights[n - 1] > W:
                self.memo[n][W] = helper(values, weights, W, n - 1)
                return self.memo[n][W]
            else:
                self.memo[n][W] = max(values[n - 1] + helper(values, weights, W - weights[n - 1], n - 1),
                        helper(values, weights, W, n - 1))
                return self.memo[n][W]
        return helper(values, weights, W, n)
values = [1, 3, 4, 5]
weights = [1, 4, 5, 7]
W = 7
n = len(values)
print(Solution().knapsack(values, weights, W, n))
            

