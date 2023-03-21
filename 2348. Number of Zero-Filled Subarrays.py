from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        idx = 0
        while idx < len(nums):
            zeroes_count = 0
            if nums[idx] == 0:
                while idx < len(nums) and nums[idx] == 0:
                    zeroes_count += 1
                    idx += 1
                count += zeroes_count
            else:
                idx += 1
            count += int((zeroes_count * (zeroes_count - 1))/2)
        return count

sol = Solution()
nums = [1, 3, 0, 0, 2, 0, 0, 4]
res = sol.zeroFilledSubarray(nums)
print(res)
