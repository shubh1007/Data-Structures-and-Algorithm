from sys import maxsize
class Solution:
    def maxSubarrayCircular(self, nums: list[int]) -> int:
        n = len(nums)
        max_straight_sum = -float("inf")
        temp_max_sum = 0
        min_straight_sum = float("inf")
        temp_min_sum = 0
        array_sum = 0
        for i in range(n):
            temp_max_sum += nums[i]
            max_straight_sum = max(max_straight_sum, temp_max_sum)
            temp_max_sum = max(temp_max_sum, 0)

            array_sum += nums[i]

            temp_min_sum += nums[i]
            min_straight_sum = min(min_straight_sum, temp_min_sum)
            temp_min_sum = min(temp_min_sum, 0)
        if array_sum == min_straight_sum:
            return max_straight_sum
        else:
            return max(max_straight_sum, array_sum - min_straight_sum)
        

sol = Solution()
nums = [1, 2, -3, -2, 6]
# nums = [5, -3, 5]
res = sol.maxSubarrayCircular(nums)
print(res)