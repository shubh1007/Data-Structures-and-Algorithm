class Solution:
    def rob(self, nums):
        """
        It will automatically contact the police if two adjacent houses were broken into on the same night.
        Given an integer array nums representing the amount of money of each house, 
        return the maximum amount of money you can rob tonight without alerting the police.

        Args:
            nums (list[int]): List of amount of money stored in the ith house.

        Returns:
            int: returns the maximum amount of money that can be rob without alerting the police.
        """
        # Iterative + 2 Variables 
        # Beats 96.26% Time Complexity
        # Beats 97.62% Space Complexity
        prev1 = 0
        prev2 = nums[0]
        for i in range(1, len(nums)):
            temp = prev2
            prev2 = max(prev1 + nums[i], prev2)
            prev1 = temp
        return prev2

        # Iterative + Memoization
        # memo = [-1 for _ in range(len(nums) + 1)]
        # memo[0] = 0
        # memo[1] = nums[0]
        # for i in range(1, len(nums)):
        #     val = nums[i]
        #     memo[i + 1] = max(memo[i - 1] + val, memo[i])
        # return memo[-1]

        # Memoization + Recursion
        # memo = [-1 for _ in range(len(nums) + 1)]
        # def helper(i):
        #     if memo[i] != -1: return memo[i]
        #     if i < 0: return 0
        #     result = max(helper(i - 2) + nums[i], helper(i - 1))
        #     memo[i] = result
        #     return result
        # return helper(len(nums) - 1)

nums = [2, 7, 9, 3, 1]
sol = Solution()
res = sol.rob(nums)
print(res)
