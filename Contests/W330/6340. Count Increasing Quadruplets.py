class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n - 3):
            for j in range(i + 1, n - 1):
                k = j + 1
                l = n - 1
                while k < l:
                    if nums[i] < nums[k] < nums[j] < nums[l]:
                        count += l - k
                        k += 1
                    else:
                        l -= 1
        return count

sol = Solution()
nums = [1,3,5,2,4]
res = sol.countQuadruplets(nums)
print(res)