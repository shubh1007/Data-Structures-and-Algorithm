class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

nums = [1, 1, 2, 3, 4, 5]
sol = Solution()
res = sol.findDuplicate(nums)
print(res)
