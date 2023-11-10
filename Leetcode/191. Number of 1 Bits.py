class Solution:
    def hammingWeight(self, n: int) -> int:
        setBitCount = 0
        while n != 0:
            n = n & (n - 1)
            setBitCount += 1
        return setBitCount