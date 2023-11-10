from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 0
        def helper(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time <= h
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
sol = Solution()
piles = [30,11,23,4,20]
h = 5
print(sol.minEatingSpeed(piles, h))