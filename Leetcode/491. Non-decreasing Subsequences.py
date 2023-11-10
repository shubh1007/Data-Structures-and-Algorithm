class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        res = set()
        n = len(nums)
        def helper(i, ds):
            if len(ds) > 1:
                res.add(tuple(ds))
            if i == n: 
                return
            if not ds or nums[i] >= ds[-1]:
                helper(i + 1, ds + [nums[i]])
            helper(i + 1, ds)
        helper(0, [])
        return res


# nums = [4, 6, 7, 7]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]
sol = Solution()
res = sol.findSubsequences(nums)
print(res)
