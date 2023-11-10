class Solution:
    def lengthOfLongestSubstring(self, s):
        charMap = {}
        left, right = 0, 0
        result = 0
        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right - left + 1)
            right += 1
        return result
        
            
            

sol = Solution()

# s = "abcabcbb"
# s = "bbbbbb"
# s = "pwwkew"


maxVal = sol.lengthOfLongestSubstring(s)
print(maxVal)

                
