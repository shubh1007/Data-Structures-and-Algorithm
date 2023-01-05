class Solution:
    def jump(self, nums):
        current = 0
        jumps = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if i == current:
                current = farthest
                jumps += 1
        return jumps
    
nums = [3, 4, 5, 2, 3, 1, 4, 2]
sol = Solution()
res = sol.jump(nums)
print(res)