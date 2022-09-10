class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num1 in range(len(nums)):
            for num2 in range(num1, len(nums)):
                if num1 != num2 and nums[num2] == (target - nums[num1]):
                    return [num1, num2]
        return []
    
    def sol2(self, nums, target):
        myHash = {}
        for i in nums:
            if (target - i) in nums:
                
                    
