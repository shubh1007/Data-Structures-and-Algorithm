import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        SUM = (n * (n + 1)) / 2
        SQRT = math.sqrt(SUM)
        if math.floor(SQRT) == math.ceil(SQRT):
            return int(SQRT)
        return -1
    
n = 8
sol = Solution()
res = sol.pivotInteger(n)
print(res)
    
        