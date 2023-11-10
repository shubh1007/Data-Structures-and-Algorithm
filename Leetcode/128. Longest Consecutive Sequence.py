class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in numSet:
                streak = 1
                temp = num
                while temp + 1 in numSet:
                    streak += 1
                    temp += 1
                res = max(res, streak)
        return res

nums = [100,4,200,1,3,2]
sol = Solution()
res = sol.longestConsecutive(nums)
print(res)