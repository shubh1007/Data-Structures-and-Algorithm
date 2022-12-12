class Solution:
    def permute(self, nums):
        """returns the Permutations of the sequence provided in the form : List[List[int]]
        Args:
            nums (int): List of numbers.

        Returns:
            List[List[int]]: Returns all possible permutations of the sequence
            Size: N!
        
        Time Complexity: O(N!)
        Space Complexity: O(N!)
        """
        if len(nums) == 1: return [nums[:]]
        result = []
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

sol = Solution()
nums = [1, 2, 3, 4, 5, 6]
result = sol.permute(nums)
print(len(result))