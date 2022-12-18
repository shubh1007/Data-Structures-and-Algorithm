class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0 for i in range(len(temperatures))]
        for idx, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                temp = stack.pop()
                res[temp[0]] = idx - temp[0]
            stack.append([idx, val])
        return res

sol = Solution()
temperatures = [89,62,70,58,47,47,46,76,100,70]
result = sol.dailyTemperatures(temperatures)
print(result)