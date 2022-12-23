class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        leftPrefix = [1] * n
        res = [1] * (n)
        for i in range(1, n):
            leftPrefix[i] = leftPrefix[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            res[i] = res[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = leftPrefix[i] * res[i]
        return res
    
sol = Solution()
nums = [1, 2, 3, 4]
res = sol.productExceptSelf(nums)
print(res)