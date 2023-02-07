def isBadVersion(num):
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        mid = (low + high) // 2
        res = mid
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
         


        
        