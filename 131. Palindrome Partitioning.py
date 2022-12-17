class Solution:
    def partition(self, s):
        result = []
        def helper(idx, ds):
            if idx == len(s):
                result.append(ds.copy())
                return 
            for i in range(idx, len(s)):
                if isPalindrome(idx, i):
                    ds.append(s[idx: i + 1])
                    helper(i + 1, ds)
                    ds.pop()
        
        def isPalindrome(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        helper(0, [])
        return result

sol = Solution()
s = "aab"
result = sol.partition(s)
for i in result:
    print(i)