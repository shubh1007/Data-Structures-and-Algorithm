from typing import List
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            count = set()
            for i in range(1, int(num ** 0.5 + 1)):
                if num % i == 0:
                    count.add(num//i)
                    count.add(i)
                    # Add 3 as well as 7 for 21
                if len(count) > 4:
                    break
            if len(count) == 4:
                res += sum(count)
        return res
