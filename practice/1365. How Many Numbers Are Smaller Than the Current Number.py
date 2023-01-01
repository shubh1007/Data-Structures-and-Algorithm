class Solution:
    def smallerNumbersThanCurrent(self, nums):
        hm = {}
        for idx, val in enumerate(nums):
            hm[idx] = val
        nums.sort()
        res = [0] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                res[i] = res[i - 1]
            else:
                res[i] = i
        return res

nums = [8, 1, 2, 2, 3]
sol = Solution()
res = sol.smallerNumbersThanCurrent(nums)
print(res)
        