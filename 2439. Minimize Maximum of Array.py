from typing import List
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total_sum = 0
        res = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            res = max(res, (total_sum + i) // (i + 1))
        return int(res)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(Solution().minimizeArrayValue(nums))