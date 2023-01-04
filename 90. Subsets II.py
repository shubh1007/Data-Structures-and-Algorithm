class Solution:
    def subsetsWithDup(self, nums):
        res = []
        def helper(i, ds):
            if i == len(nums):
                res.append(ds.copy())
                return
            ds.append(nums[i])
            helper(i + 1, ds)
            ds.pop()

            if not ds or ds[-1] != nums[i]:
                helper(i + 1, ds)
        nums.sort()
        helper(0, [])
        return res


sol = Solution()
nums = [1, 2, 2]
res = sol.subsetsWithDup(nums)
print(res)