class Solution:
    def shuffle(self, nums, n: int):
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res

sol = Solution()
nums = [2, 5, 1, 3, 4, 7]
n = 3
res = sol.shuffle(nums, n)
print(res)
