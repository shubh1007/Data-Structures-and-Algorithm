from typing import List
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            count = set()
            for j in range(1, int(i **0.5 + 1)):
                if i % j == 0:
                    count.add(i // j)
                    count.add(j)
                if len(count) > 4:
                    break
            if len(count) == 4:
                res += sum(count)

        return res