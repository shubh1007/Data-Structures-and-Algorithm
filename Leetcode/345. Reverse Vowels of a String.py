class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            if s[left] in ['a','e','i','o','u', "A", "E", "I", "O", "U"] and s[right] in ['a','e','i','o','u',"A", "E", "I", "O", "U"]:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1 
            elif s[left] not in ['a','e','i','o','u', "A", "E", "I", "O", "U"]:
                left += 1
            else:
                right -= 1
        res = "".join(x for x in s)
        return res
        
                
                
                
            
