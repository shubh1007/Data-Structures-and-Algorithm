from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right, flag = 0, len(nums) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                flag = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if flag == -1:
            return [-1, -1]
        left, right = flag, flag 
        while left >= 0 and nums[left] == target :
            left -= 1
        while right < len(nums) and nums[right] == target :
            right += 1
        return [left + 1, right - 1]
        
            
            