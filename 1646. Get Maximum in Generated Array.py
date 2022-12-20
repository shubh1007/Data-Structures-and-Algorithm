class Solution:
    def getMaximumGenerated(self, n):
        if n < 2:
            return n
        nums    = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        i = 1
        while 2*i <= n:
            if 2*i <= n:
                nums[i*2] = nums[i]
            if (2 * i + 1) <= n:
                nums[2*i+1] = nums[i] + nums[i+1]
            i += 1
        print(nums)
        return max(nums)

sol = Solution()
n = 7
res = sol.getMaximumGenerated(n)
print(res)
