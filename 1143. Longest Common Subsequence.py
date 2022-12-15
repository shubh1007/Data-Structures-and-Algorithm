class Solution:
    def longestCommonSubsequence(self, text1, text2):
        # SHOWING ERROR FOR SOME INPUTS
        # prev = [0 for _ in range(len(text2) + 1)]
        # curr = [0 for _ in range(len(text2) + 1)]
        # for i in range(1, len(text1) + 1):
        #     for j in range(1, len(text2) + 1):
        #         if text1[i - 1] == text2[j - 1]:
        #             curr[j] = 1 + prev[j - 1]
        #         else:
        #             curr[j] = max(prev[j], curr[j - 1])
        #     prev = curr
        # return prev[len(text2)]


        # Tabulation + Stack Space Optimized
        dp = [[-1 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(len(text1) + 1): dp[i][0] = 0
        for i in range(len(text2) + 1): dp[0][i] = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(text1)][len(text2)]



        # Tabulation + Memoization
        # dp = [[-1 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        # def helper(i, j):
        #     if i == 0 or j == 0: 
        #         dp[i][j] = 0
        #         return dp[i][j]
        #     if dp[i][j] != -1: 
        #         return dp[i][j]
        #     if text1[i - 1] == text2[j - 1]:
        #         dp[i][j] = 1 + helper(i - 1, j - 1)
        #         return dp[i][j]
        #     else:
        #         dp[i][j] = max(helper(i - 1, j), helper(i, j - 1))
        #         return dp[i][j]
        # return helper(len(text1), len(text2))
          
        # Memoization
        # dp = {}
        # def helper(i, j):
        #     if i < 0 or j < 0: return 0
        #     if (i, j) in dp: return dp[(i, j)]
        #     if text1[i] == text2[j]: 
        #         return 1 + helper( i - 1, j - 1)
        #     else:
        #         dp[(i, j)] = max(helper(i, j - 1), helper(i - 1, j))
        #         return dp[(i, j)]
        # return helper(len(text1) - 1, len(text2) - 1)

sol = Solution()
text1 = "abcba"
text2 = "abcbcba"
result = sol.longestCommonSubsequence(text1, text2)
print(f"The longest common subsequence : {result}")