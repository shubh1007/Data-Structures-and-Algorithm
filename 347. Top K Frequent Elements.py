class Solution:
    def topKFrequent(self, nums, k):
        res = []
        count = {}
        for i in nums:
            if i not in count: count[i] = 1
            else: count[i] += 1
        
        for key, val in count.items():
            res.append((key, val))
        res.sort(key = lambda x: x[1], reverse= True)
        print(res)
        result = []
        for i in range(k):
            result.append(res[i][0])
        return result
    

nums = [1, 1, 1, 2, 2, 2, 3, 4, 3]
k = 3
sol = Solution()
result = sol.topKFrequent(nums, k)
print(result)
