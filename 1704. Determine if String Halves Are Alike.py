class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)-1
        a, b = s[:(n//2)+1], s[(n//2)+1:]
        vA, vB = 0, 0
        for i in a:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                vA += 1
        for i in b:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                vB += 1
        return vA == vB
