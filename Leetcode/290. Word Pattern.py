class Solution:
    def wordPattern(self, pattern, s):
        s = s.split()
        hm = {}
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if pattern[i] not in hm:
                hm[pattern[i]] = s[i]
            else:
                if hm[pattern[i]] != s[i]:
                    return False
        return True

sol = Solution()
pattern = "abba"
s = "dog cat cat fish"
res = sol.wordPattern(pattern, s)
print(res)

