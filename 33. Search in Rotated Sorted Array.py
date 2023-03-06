class Solution:
    def search(self, nums: list[int], target: int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # Target Found
                return mid
            elif nums[mid] >= nums[left]:
                # Left part is sorted
                if (target > nums[mid]) or (target < nums[mid] and target < nums[left]):
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # Right part is sorted
                if (target < nums[mid]) or (target > nums[mid] and target > nums[right]):
                    right = mid - 1
                else:
                    left = mid + 1
        return -1