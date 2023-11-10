import bisect

class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res = []
        for q in queries:
            idx = bisect.bisect_right(nums, q)
            res.append(idx)
        return res

num = [4, 5, 2, 1]
queries = [3, 10, 21]
sol = Solution()
res = sol.answerQueries(num, queries)
print(res)



        

