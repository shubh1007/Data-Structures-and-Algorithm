class Solution:
    def rob(self, nums):
        memo = [-1 for _ in range(len(nums) + 1)]
        def helper(i):
            if memo[i] != -1: return memo[i]
            if i < 0: return 0
            result = max(helper(i - 2) + nums[i], helper(i - 1))
            memo[i] = result
            return result
        return helper(len(nums) - 1)

nums = [2, 7, 9, 3, 1]
sol = Solution()
res = sol.rob(nums)
print(res)
