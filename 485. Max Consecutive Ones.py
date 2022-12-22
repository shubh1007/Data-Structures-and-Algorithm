class Solution:
    def findMaxConsecutiveOnes(self, nums):
        res = 0
        count = 0
        for i in nums:
            if i == 0:
                count = 0
            else:
                count += 1
            res = max(res, count)
        return res
    
sol = Solution()
nums = [1,0,1,1,0,1]
res = sol.findMaxConsecutiveOnes(nums)
print(res)