class Solution:
    def rob(self, nums):
        self.track = 0
        def helper(i):
            if i < 0: return 0
            return max(helper(i - 2) + nums[i], helper(i - 1))
        return helper(len(nums) - 1)
        

nums = [1, 2, 3, 1]
sol = Solution()
res = sol.rob(nums)
print(res)
