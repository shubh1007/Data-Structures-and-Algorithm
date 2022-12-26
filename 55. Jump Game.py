class Solution:
    def canJump(self, nums):
        n = len(nums)
        goal = nums[-1]
        for i in range(n - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0


sol = Solution()
nums = [0, 2, 1, 10, 4]
res = sol.canJump(nums)
print(res)