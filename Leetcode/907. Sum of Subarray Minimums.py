class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        res = preSum = 0
        for idx, val in enumerate(arr):
            count = 1
            while stack and stack[-1][0] >= val:
                v, c = stack.pop()
                count += c
                preSum -= v * c
            stack.append((val, count))
            preSum += val * count
            res += preSum 
        return res % MOD
