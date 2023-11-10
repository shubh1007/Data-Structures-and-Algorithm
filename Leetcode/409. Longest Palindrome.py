class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        for char in s:
            if char not in letters: letters[char] = 1
            else: letters[char] += 1
        
        res, odd = 0, 0
        
        if len(letters) == 1: return letters[s[0]]
        
        for i in letters.values():
            if i>1:
                if i%2 == 0:
                    res += i
                else:
                    res += i - 1
                    odd += 1
            else:odd += 1
        if odd > 0: res += 1
        return res
            
            
                    