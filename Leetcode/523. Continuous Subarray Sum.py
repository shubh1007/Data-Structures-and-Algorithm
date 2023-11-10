class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        memo = {0:-1}
        totalSum = 0
        for idx, ele in enumerate(nums):
            totalSum += ele
            rem = totalSum % k
            
            if rem not in memo:
                memo[rem] = idx
            elif idx - memo[rem] > 1:
                return True
        return False
