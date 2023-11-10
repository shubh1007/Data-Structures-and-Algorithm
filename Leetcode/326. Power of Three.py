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
<<<<<<< HEAD
print(sol.isPowerOfThree(n))
=======
print(sol.isPowerOfThree(n))
>>>>>>> 0054b6a7878fe0f5d064104af0559b659008e036
