class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0
        for idx in range(len(gas)):
            tank += gas[idx] - cost[idx]
            if tank < 0:
                tank = 0
                start = idx + 1
        return start


sol = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
res = sol.canCompleteCircuit(gas, cost)
print(res)