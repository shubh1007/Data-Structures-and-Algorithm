class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0]*len(temperatures)
        for idx in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                temp = stack.pop()
                res[temp] = idx - temp
            stack.append(idx)
        return res

sol = Solution()
temperatures = [89,62,70,58,47,47,46,76,100,70]
result = sol.dailyTemperatures(temperatures)
print(result)