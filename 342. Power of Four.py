import math

class Solution:
    def isPowerOfFour(self, n):
        if n <= 0: return False
        res = math.log(n)/ math.log(4)
        if math.floor(res) == math.ceil(res): return True
        return False

sol = Solution()
n = [16, 5, 1, -2147483648, 0]
for i in n:
    if i < 0:
        i *= -1
    print(sol.isPowerOfFour(i))