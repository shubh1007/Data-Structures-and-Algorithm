import heapq
from typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            temp = heapq.heappop(nums)
            heapq.heappush(nums, -temp)
        SUM = sum(nums)
        return SUM
        
