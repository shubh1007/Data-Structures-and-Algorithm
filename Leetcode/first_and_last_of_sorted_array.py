class Solution:
    def searchRange(self, nums, target):
        result = [-1, -1]
        lb, ub = 0, len(nums) - 1
        flag = -1
        while lb <= ub and flag == -1:
            mid = (lb + ub)//2
            if nums[mid] == target:
                flag = mid
                break
            elif nums[mid] > target:
                ub = mid - 1
            else:
                lb = mid + 1
        if flag != -1:
            left, right = flag, flag
            while nums[left] == target and left >= 0:
                left -= 1
                
            while right < len(nums) and nums[right] == target:
                right += 1
            result = [left+1, right-1]
            return result
        else:
            return [-1, -1]


sol = Solution()
nums = [1]
target = 1
result = sol.searchRange(nums, target)
print(result)
            
        
