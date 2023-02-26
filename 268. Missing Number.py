class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return abs(sum(nums) - (n*(n+1))//2)