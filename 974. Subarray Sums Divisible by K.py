class Solution:
    def subarraysDivByK(self, nums, k):
        hm = {}
        SUM = 0
        ans = 0
        hm[0] = 1
        for i in range(len(nums)):
            SUM += nums[i]
            rem = SUM % k
            if rem < 0:
                rem += k
            if rem in hm:
                ans += hm[rem]
                hm[rem] += 1
            else:
                hm[rem] = 1
        return ans

sol = Solution()
nums = [4, 5, 0, -2, -3, 1]
k = 5
res = sol.subarraysDivByK(nums, k)
print(res)
