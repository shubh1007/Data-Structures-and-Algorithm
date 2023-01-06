class Solution:
    def maxIceCream(self, costs, coins):
        costs.sort()
        res = 0
        for i in costs:
            if coins <= 0:
                return res
            if i <= coins:
                res += 1
                coins -= i
        return res
        