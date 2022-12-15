class Solution:
    def permute(self, nums):
        if len(nums) == 1: return [nums[:]]
        result = []
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

nums = [1, 2, 3, 4, 1, 2]
sol = Solution()
result = sol.permute(nums)

for i in result:
    print(i)
print(len(result))