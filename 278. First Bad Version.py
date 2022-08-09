
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lb = 1
        ub = n
        res = n
        while(lb<=ub):
            mid = (lb+ub)//2
            if (isBadVersion(mid)):
                res = mid
                ub = mid-1
            else:
                lb = mid+1
        return res
                
        
