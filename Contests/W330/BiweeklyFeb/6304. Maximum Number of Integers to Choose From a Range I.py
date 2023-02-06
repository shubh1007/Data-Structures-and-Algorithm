class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        arr1 = [i for i in range(1, n + 1) if i not in banned]
        left, right = 0, len(arr1) - 1
        res = 0
        while left != right and left < len(arr1) and right >= 0:
            if arr1[left] + arr1[right] <= maxSum:
                print(arr1[left: right])
                res = max(res, right - left + 1)
                left += 1
            right -= 1
        return res
                
banned = [1, 6, 5]
n = 5
maxSum = 6
sol = Solution()
res = sol.maxCount(banned, n, maxSum)
print(res)
