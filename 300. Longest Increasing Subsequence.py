class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 1
        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        for i in range(1, len(nums)):
            arrMax = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[j] > arrMax:
                        arrMax = dp[j]
            dp[i] = arrMax + 1
            if dp[i] > maxLen: 
                maxLen = dp[i]
        return maxLen