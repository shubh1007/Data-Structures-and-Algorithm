from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        res = []
        for i in range(len(nums)):
            if q and i - k == q[0]:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res









nums = [1, -1]
k = 1
sol = Solution()
res = sol.maxSlidingWindow(nums, k)
print(res)
