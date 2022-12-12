class Solution:
    def permute(self, nums):
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
nums = [1, 2, 3]
result = sol.permute(nums)
for i in result:
    print(i)