class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        ans = []
        for i in matrix:
            for j in i:
                ans.append(j)
        ans.sort()
        return ans[k-1]