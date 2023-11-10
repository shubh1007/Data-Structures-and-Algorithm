class Solution:
    def longestPalindrome(self, s):
        result = ""
        n = len(s)
        dp = [[0 for i in range(n)] for i in range(n)]
        maxLen = 0
        for i in range(n):
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if maxLen < right - left + 1:
                    result = s[left: right + 1]
                    maxLen = right - left + 1
                left -= 1
                right += 1
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > maxLen:
                    result = s[left: right + 1]
                    maxLen = right - left + 1
                left -= 1
                right += 1
        return result
        
    
                   
        """
        result = ""
        maxLen = 0
        i, j, diff = 0, 0, 0
        n = len(s)
        dp = [[0 for i in range(n)] for i in range(n)]
        while diff < n:
            j = diff
            i = 0
            while j < n:
                if i == j:
                    dp[i][j] = 1
                elif diff == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                else:
                    if dp[i+1][j-1] and s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                        
                if dp[i][j] > maxLen:
                    maxLen = dp[i][j]
                    result = s[i: j+1]

                i += 1
                j += 1
                
            diff += 1
        return result
        """ 
                



sol = Solution()
s = "abcdcba"
print(len(s))
result = sol.longestPalindrome(s)
print(f"{len(result)} : {result}")





exit()



        
        

        
                
                

"""
sol = Solution()
s = "cbbd"
result = sol.longestPalindrome(s)
print(result)
"""


class Solution2:
    def longestPalindrome(self, s):
        result = ""
        n = len(s)
        dp = [[0 for i in range(n)] for i in range(n)]
        i, j = 0, 0
        diff = 0
        maxLen = 0
        result = ""
        while diff < n:
            j = diff
            i = 0
            while j < n:
                
                if i == j:
                    dp[i][j] = 1
                elif diff == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = dp[i + 1][j - 1] + 2

                if dp[i][j]:
                    if (j - i + 1) > maxLen:
                        maxLen = j - i + 1
                        result = s[i:j+1]
                i += 1
                j += 1
            diff += 1
        return result
                
            
        
sol = Solution2()
s = "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
print(len(s))
result = sol.longestPalindrome(s)
print(f"{len(result)} : {result}")











