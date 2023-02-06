class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastFoundNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastFoundNonZero] = nums[i]
                lastFoundNonZero += 1
        for i in range(lastFoundNonZero, len(nums)):
            nums[i] = 0
        
        
        
            
        
nums = [0,0, 1]
sol = Solution()
res = sol.moveZeroes(nums)
print(nums)
