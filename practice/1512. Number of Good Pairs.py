class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] += 1
            else:
                hm[nums[i]] = 1
        for element, count in hm.items():
            if count > 1:
                count += count*(count - 1)//2
        return count

nums = [1,2,3,1,1,3]
sol = Solution()
res = sol.numIdenticalPairs(nums)
print(res)
