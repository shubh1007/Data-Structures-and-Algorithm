class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = [0 for i in range(len(nums))]
        right = [0 for i in range(len(nums))]
        SUM = nums[0]
        left[0] = nums[0]
        for i in range(1, len(nums)):
            SUM += nums[i]
            left[i] = SUM
        SUM = nums[-1]
        n = len(nums)
        right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            SUM += nums[i]
            right[i] = SUM
        
        for i in range(len(nums)):
            if left[i] == right[i]: return i
        return -1

sol = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(sol.pivotIndex(nums))