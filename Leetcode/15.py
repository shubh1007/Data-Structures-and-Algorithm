# 3Sum

class Solution:
    def threeSum(self, nums):
        N = len(nums)
        res = []
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        return res

nums = [-1,0,1,2,-1,-4]
sol = Solution()
result = sol.threeSum(nums)
print(result)



