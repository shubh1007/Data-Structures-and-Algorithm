class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        len_row = len(nums1) + 1
        len_col = len(nums2) + 1
        
        dp = [[0 for _ in range(len_col)] for _ in range(len_row)]
        
        for i in range(1, len_row):
            for j in range(1, len_col):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        
        return max(max(row) for row in dp)
