class Solution:
    def sortColors(self, nums):
        left, right = 0, len(nums) - 1
        idx = 0
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        while idx <= right:
            if nums[idx] == 0:
                swap(left, idx)
                left += 1
            elif nums[idx] == 2:
                swap(right, idx)
                right -= 1
                idx -= 1
            idx += 1

sol = Solution()
nums = [1, 0, 1, 2, 2]
sol.sortColors(nums)
print(nums)