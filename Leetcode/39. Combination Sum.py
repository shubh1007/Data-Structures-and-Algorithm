class Solution:
    def combinationSum(self, candidates, target):
        self.result = []
        def helper(idx, target, ds):
            if idx == len(candidates): 
                if target == 0:
                    self.result.append(ds.copy())
                return
            if candidates[idx] <= target:
                ds.append(candidates[idx])
                helper(idx, target - candidates[idx], ds)
                ds.pop()
            helper(idx + 1, target, ds)
        ds = []
        helper(0, target, ds)
        return self.result

sol = Solution()
candidates = [1, 2, 3]
target = 7
result = sol.combinationSum(candidates, target)
print(result)