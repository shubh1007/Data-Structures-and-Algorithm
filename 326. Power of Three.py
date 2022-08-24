import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        while n % 3 == 0: n = n / 3
        return n == 1




sol = Solution()
n = 243
print(sol.isPowerOfThree(n))