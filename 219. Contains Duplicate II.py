class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in indexMap and i - indexMap[num] <= k:
                return True
            indexMap[num] = i
        return False
